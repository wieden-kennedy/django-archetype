from archetype import views
from django.conf.urls.defaults import *
from django.conf import settings
import dselector

parser = dselector.Parser()
url = parser.url


urlpatterns = parser.patterns('',
    url(r'archetype-test', views.test, name='test'),
    url(r'^robots.txt',     views.robots_txt,          name='robots_txt'),
    url(r'^always-500',     views.always_500,          name='always_500'),
)

try:
    if settings.FAVICON_URL != "":
        urlpatterns += patterns('',
            (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.FAVICON_URL}),
        )
except:
    pass
