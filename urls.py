
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns("",
    ("^admin/", include(admin.site.urls)),
    url("", include("social_auth.urls")),
    url("", include("core.urls")),
)