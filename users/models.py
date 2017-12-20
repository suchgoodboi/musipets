from django.db import models
from django.contrib.auth.models import AbstractUser
from users.validators import validate_facebook_url
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
import os


class OwnerProfile(AbstractUser):
    is_information_confirmed = models.BooleanField(default=False)
    facebook = models.URLField(max_length=250, blank=True, null=True,
                               validators=[validate_facebook_url])
    phone = models.CharField('Telefone', max_length=30, blank=True)
    profile_picture = models.ImageField(upload_to='user_profiles',
                                        help_text=_('Maximum image size is 8MB'),
                                        default=os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/static/img/caaaat.png')

    def get_absolute_url(self):
        return reverse('users:user_profile', args=[self.id])

    def __str__(self):
        return self.username
# CREATE TABLE test_users (id int, first_name VARCHAR(50), second_name VARCHAR(50), mail VARCHAR(50), count_songs int);

# class Musicants(AbstractUser):
#     f_name = models.CharField(max_length=50)
#     s_name = models.CharField(max_length=50)
#     mail = models.CharField(max_length=50)
#     count_songs = models.CharField(max_length=50)