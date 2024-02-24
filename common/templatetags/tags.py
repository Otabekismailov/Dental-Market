from django import template
from django.conf import settings

from common.models import WEEKDAYS_EN, WEEKDAYS_UZ, WEEKDAYS_RU

register = template.Library()


@register.filter()
def split(value):
    parts = value.split()  # Split the value into parts
    part_1 = ' '.join(parts[:3])  # Join the first three parts with a space
    part_2 = ' '.join(parts[3:])  # Join the remaining parts with a space
    return part_1, part_2


@register.filter()
def weekdays__(value, lang):
    f = ''
    t = ''
    if lang == 'uz':

        for k, v in WEEKDAYS_UZ:
            if k == value.from_weekday_uz:
                f += v
            if k == value.to_weekday_uz:
                t += v
        return f, t
    elif lang == 'ru':
        for k, v in WEEKDAYS_RU:
            if k == value.from_weekday_ru:
                f += v
            if k == value.to_weekday_ru:
                t += v
        return f, t
    elif lang == 'en':
        for k, v in WEEKDAYS_EN:
            if k == value.from_weekday_en:
                f += v
            if k == value.to_weekday_en:
                t += v
        return f, t


@register.simple_tag
def get_from_settings(key, default=None):
    return getattr(settings, key, default)