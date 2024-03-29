from __future__ import unicode_literals

from django.core.checks import Warning

from yacms.conf import settings


def check_context_processor(app_configs, **kwargs):

    issues = []

    name = 'yacms.pages.context_processors.page'

    if settings.TEMPLATES:
        loaded = any(name in config.get('OPTIONS', {}).get(
            'context_processors', {}) for config in settings.TEMPLATES)
    else:
        loaded = name in settings.TEMPLATE_CONTEXT_PROCESSORS

    if not loaded:
        issues.append(Warning(
            "You haven't included 'yacms.pages.context_processors.page' "
            "as a context processor in any of your template configurations. "
            "Your templates might not work as expected.",
            id="yacms.pages.W01"
        ))

    return issues
