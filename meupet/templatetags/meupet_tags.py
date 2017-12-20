from django import template
from django.template.loader import render_to_string

from meupet.models import Song

register = template.Library()


@register.simple_tag()
def sidemenu():
    return render_to_string('meupet/_sidemenu.html', {
        'url': Song.get_absolute_url(),
    })
