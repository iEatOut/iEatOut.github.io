from django.conf.urls import patterns, url
from ieatout import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'), 
    url(r'^result/$', views.result, name='result'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_url>\w+)$', views.index, name='index'),
)
urlpatterns += staticfiles_urlpatterns()
