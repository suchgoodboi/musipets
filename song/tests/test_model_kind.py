from django.test import TestCase

from song.models import Kind


class KindModelTest(TestCase):
    def test_slug(self):
        kind = Kind.objects.create(kind='Dog')

        self.assertEqual('dog', kind.slug)

    def test_unique_kind(self):
        kind_field = Kind._meta.get_field('kind')

        self.assertTrue(kind_field.unique)
