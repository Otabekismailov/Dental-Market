from .models import About, ClinicMember, Partners, Products, Testimonial, TestimonialUser, Banners
from modeltranslation.translator import TranslationOptions, register


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(ClinicMember)
class ClinicMemberTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Partners)
class PartnersTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description',)


@register(Products)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description',)


@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(TestimonialUser)
class TestimonialUserTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Banners)
class BannersTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description',)
