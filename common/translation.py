from .models import About, ClinicMember, Services, Products
from modeltranslation.translator import TranslationOptions, register


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ClinicMember)
class ClinicMemberTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description',)


@register(Products)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description',)
