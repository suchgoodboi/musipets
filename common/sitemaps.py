from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse

from song.models import Song


class SongEntrySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return Song.objects.all()

    @staticmethod
    def lastmod(obj):
        return obj.modified


class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1.0
    protocol = 'http'

    def items(self):
        return [
            'common:homepage',
            'common:about',
            'song:index',
            'song:search',
        ]

    def location(self, item):
        return reverse(item)
