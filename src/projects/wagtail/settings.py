from sandbox.settings import *

INSTALLED_APPS += [
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',
    'projects.wagtail.apps.WagtailSandboxConfig'
]

MIDDLEWARE += [
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'projects.wagtail.urls'

WAGTAIL_SITE_NAME = 'Wagtail Sandbox'
