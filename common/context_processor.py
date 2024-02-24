from django.shortcuts import render

from common.models import About
from django.conf import settings


class Lenguage:
    Uzbek = 'uz'
    Russion = 'ru'
    English = 'en'


def lang_context_processor(request):
    return {'LANG': request.LANGUAGE_CODE}


def ga_tracking_id(request):
    return {'ga_tracking_id': settings.GA_TRACKING_ID}


def use_ga(request):
    return {'use_ga': settings.USE_GA}


def facebook_id(request):
    return {'facebook_pixel_id': settings.FACEBOOK_PIXEL_ID}
