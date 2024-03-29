"""
This is the main ``urlconf`` for yacms - it sets up patterns for
all the various yacms apps, third-party apps like Grappelli and
filebrowser.
"""

from __future__ import unicode_literals
from future.builtins import str

from django.conf.urls import include, url
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import javascript_catalog
from django.http import HttpResponse

from yacms.conf import settings
from yacms.core.sitemaps import DisplayableSitemap


urlpatterns = []

# JavaScript localization feature
js_info_dict = {'domain': 'django'}
urlpatterns += [
    url(r'^jsi18n/(?P<packages>\S+?)/$', javascript_catalog, js_info_dict),
]

if settings.DEBUG and "debug_toolbar" in settings.INSTALLED_APPS:
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]

# Django's sitemap app.
if "django.contrib.sitemaps" in settings.INSTALLED_APPS:
    sitemaps = {"sitemaps": {"all": DisplayableSitemap}}
    urlpatterns += [
        url("^sitemap\.xml$", sitemap, sitemaps),
    ]

# Return a robots.txt that disallows all spiders when DEBUG is True.
if getattr(settings, "DEBUG", False):
    urlpatterns += [
        url("^robots.txt$",
            lambda r: HttpResponse("User-agent: *\nDisallow: /",
                                   content_type="text/plain")),
    ]

# Miscellanous yacms patterns.
urlpatterns += [
    url("^", include("yacms.core.urls")),
    url("^", include("yacms.generic.urls")),
]

# yacms's Accounts app
if "yacms.accounts" in settings.INSTALLED_APPS:
    # We don't define a URL prefix here such as /account/ since we want
    # to honour the LOGIN_* settings, which Django has prefixed with
    # /account/ by default. So those settings are used in accounts.urls
    urlpatterns += [
        url("^", include("yacms.accounts.urls")),
    ]

# yacms's Blog app.
blog_installed = "yacms.blog" in settings.INSTALLED_APPS
if blog_installed:
    BLOG_SLUG = settings.BLOG_SLUG.rstrip("/")
    if BLOG_SLUG:
        BLOG_SLUG += "/"
    blog_patterns = [
        url("^%s" % BLOG_SLUG, include("yacms.blog.urls")),
    ]
    urlpatterns += blog_patterns

# yacms's Pages app.
PAGES_SLUG = ""
if "yacms.pages" in settings.INSTALLED_APPS:
    # No BLOG_SLUG means catch-all patterns belong to the blog,
    # so give pages their own prefix and inject them before the
    # blog urlpatterns.
    if blog_installed and not BLOG_SLUG.rstrip("/"):
        PAGES_SLUG = getattr(settings, "PAGES_SLUG", "pages").strip("/") + "/"
        blog_patterns_start = urlpatterns.index(blog_patterns[0])
        urlpatterns[blog_patterns_start:len(blog_patterns)] = [
            url("^%s" % str(PAGES_SLUG), include("yacms.pages.urls")),
        ]
    else:
        urlpatterns += [
            url("^", include("yacms.pages.urls")),
        ]
