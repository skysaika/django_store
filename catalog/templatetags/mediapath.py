import os

from django import template
from django.conf import settings

register = template.Library()


COMING_SOON_IMAGE_URL = os.path.join(settings.STATIC_URL, 'images/coming_soon.jpg')

@register.filter()
def mediapath(value):
    if value:
        return f"{settings.MEDIA_URL}{value}"
    return COMING_SOON_IMAGE_URL

@register.simple_tag()
def mediapath_tag(image):
    return f"{settings.MEDIA_URL}{image}"
