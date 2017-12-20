from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap

from . import views
from .sitemaps import SongEntrySitemap, PageSitemap

sitemaps = {
    'pages': PageSitemap,
    'songs': SongEntrySitemap,
}

urlpatterns = [
    url(r'^$', views.home, name='homepage'),
    url(r'^sobre/$', views.AboutPageView.as_view(), name='about'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.сдеviews.sitemap'),
]
