from django.test import TestCase
from model_mommy import mommy

from song.context_processors import pets_count
from song.models import Pet


class ContextProcessorsTestCase(TestCase):
    def setUp(self):
        mommy.make(Pet)
        mommy.make(Pet, active=False)

    def test_pets_count(self):
        context = pets_count({})

        self.assertEqual(2, context['pets_count'])
