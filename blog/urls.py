from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'post/(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'archive/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.day_archive, name='day_archive'),
    url(r'archive/(?P<year>\d{4})/(?P<month>\d{1,2})/page/(?P<page>\d)$', views.month_archive, name='month_archive'),
    url(r'archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.month_archive, name='month_archive'),
    url(r'archive/(?P<year>\d{4})/page/(?P<page>\d)$', views.year_archive, name='year_archive'),
    url(r'archive/(?P<year>\d{4})$', views.year_archive, name='year_archive'),
    url(r'$', views.index, name='index'),
    url(r'page/(?P<page>\d)$', views.index, name='index'),
]
