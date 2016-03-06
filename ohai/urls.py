from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ohai_kit.urls', namespace='ohai_kit')),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
    ]
