from django.conf.urls.defaults import *
import dselector

from sample_app import views

parser = dselector.Parser()
url = parser.url


urlpatterns = parser.patterns('',
    url(r'', views.home, name='home'),
)
