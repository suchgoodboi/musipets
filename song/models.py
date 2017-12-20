import hashlib

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone, crypto
from django.utils.text import slugify

from autoslug import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from song import services
from users.models import OwnerProfile


class SongQuerySet(models.QuerySet):

    def get_unpublished_pets(self):
        return self.filter(published=False)


class Group(models.Model):
    name = models.TextField(max_length=100, unique=True)
    genre = models.TextField(max_length=100)
    slug = AutoSlugField(max_length=30)
    image = models.ImageField(upload_to='group_photos')

    def __str__(self):
        return self.name


def get_slug(instance):
    group = ''
    if instance.group:
        group = instance.city.name
    return slugify('{}-{}'.format(instance.name, group))


class Song(TimeStampedModel):
    owner = models.ForeignKey(OwnerProfile)
    group = models.ForeignKey(Group)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    slug = AutoSlugField(max_length=50, populate_from=get_slug, unique=True)

    objects = SongQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('song:detail', kwargs={'pk_or_slug': get_slug})

    def request_action(self):
        hash_input = (crypto.get_random_string(5) + self.name).encode('utf-8')
        self.request_key = hashlib.sha1(hash_input).hexdigest()

        if not services.send_request_action_email(self):
            return

        self.request_sent = timezone.now()
        self.save(update_modified=False)

        self.active = False
        self.save(update_modified=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Photo(models.Model):
    group = models.ForeignKey(Group)
    image = models.ImageField(upload_to='group_photos')


# CREATE TABLE test_songs (id int, song_name VARCHAR(50), group_name VARCHAR(50), song_text VARCHAR(2000),


# class Songs(models.Model):
#     song_name = models.CharField(max_length=50)
#     group_name = models.CharField(max_length=50)
#     song_text = models.CharField(max_length=2000)
#     song_accords = models.CharField(max_length=100)

# CREATE TABLE test_groups (id INT, group_name VARCHAR(50), genre VARCHAR(50), group_members VARCHAR(200),
# image_url VARCHAR(250), description VARCHAR(500));

# class Groups(models.Model):
    #     group_name = models.CharField(max_length=50)
    #     genre = models.CharField(max_length=50)
    #     group_members = models.CharField(max_length=50)
    #     image_url = models.CharField(max_length=50)
    #     description = models.CharField(max_length=500)