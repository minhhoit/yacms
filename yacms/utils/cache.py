from __future__ import unicode_literals

from hashlib import md5
from inspect import getmro
from time import time

from django.core.cache import cache
from django.utils.lru_cache import lru_cache
from django.utils.cache import _i18n_cache_key_suffix
from django.utils.module_loading import import_string

from yacms.conf import settings
from yacms.utils.deprecation import get_middleware_setting
from yacms.utils.device import device_from_request
from yacms.utils.sites import current_site_id


def _hashed_key(key):
    """
    Hash keys when talking directly to the cache API, to avoid
    keys longer than the backend supports (eg memcache limit is 255)
    """
    return md5(key.encode("utf-8")).hexdigest()


def cache_set(key, value, timeout=None, refreshed=False):
    """
    Wrapper for ``cache.set``. Stores the cache entry packed with
    the desired cache expiry time. When the entry is retrieved from
    cache, the packed expiry time is also checked, and if past,
    the stale cache entry is stored again with an expiry that has
    ``CACHE_SET_DELAY_SECONDS`` added to it. In this case the entry
    is not returned, so that a cache miss occurs and the entry
    should be set by the caller, but all other callers will still get
    the stale entry, so no real cache misses ever occur.
    """
    if timeout is None:
        timeout = settings.CACHE_MIDDLEWARE_SECONDS
    refresh_time = timeout + time()
    real_timeout = timeout + settings.CACHE_SET_DELAY_SECONDS
    packed = (value, refresh_time, refreshed)
    return cache.set(_hashed_key(key), packed, real_timeout)


def cache_get(key):
    """
    Wrapper for ``cache.get``. The expiry time for the cache entry
    is stored with the entry. If the expiry time has past, put the
    stale entry back into cache, and don't return it to trigger a
    fake cache miss.
    """
    packed = cache.get(_hashed_key(key))
    if packed is None:
        return None
    value, refresh_time, refreshed = packed
    if (time() > refresh_time) and not refreshed:
        cache_set(key, value, settings.CACHE_SET_DELAY_SECONDS, True)
        return None
    return value


@lru_cache(maxsize=None)
def cache_installed():
    """
    Returns ``True`` if a cache backend is configured, and the
    cache middleware classes or subclasses thereof are present.
    This will be evaluated once per run, and then cached.
    """
    has_key = bool(getattr(settings, "NEVERCACHE_KEY", ""))

    def flatten(seqs):
        return (item for seq in seqs for item in seq)

    middleware_classes = map(import_string, get_middleware_setting())
    middleware_ancestors = set(flatten(map(getmro, middleware_classes)))

    yacms_cache_middleware_classes = {
        import_string("yacms.core.middleware.UpdateCacheMiddleware"),
        import_string("yacms.core.middleware.FetchFromCacheMiddleware"),
    }

    return (has_key and settings.CACHES and not settings.TESTING and
            yacms_cache_middleware_classes.issubset(middleware_ancestors))


def cache_key_prefix(request):
    """
    Cache key for yacms's cache middleware. Adds the current
    device and site ID.
    """
    cache_key = "%s.%s.%s." % (
        settings.CACHE_MIDDLEWARE_KEY_PREFIX,
        current_site_id(),
        device_from_request(request) or "default",
    )
    return _i18n_cache_key_suffix(request, cache_key)


def nevercache_token():
    """
    Returns the secret token that delimits content wrapped in
    the ``nevercache`` template tag.
    """
    return "nevercache." + settings.NEVERCACHE_KEY


def add_cache_bypass(url):
    """
    Adds the current time to the querystring of the URL to force a
    cache reload. Used for when a form post redirects back to a
    page that should display updated content, such as new comments or
    ratings.
    """
    if not cache_installed():
        return url
    hash_str = ""
    if "#" in url:
        url, hash_str = url.split("#", 1)
        hash_str = "#" + hash_str
    url += "?" if "?" not in url else "&"
    return url + "t=" + str(time()).replace(".", "") + hash_str
