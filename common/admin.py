from django.contrib import admin

from common.models import Weekdays, Weekends, About, ClinicMember, Services, Products, Contacts, ApplicationForm
from django.utils.text import slugify, gettext_lazy as _
from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(Weekdays)
class WeekdaysAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'from_weekday_uz', 'to_weekday_uz', 'from_weekday_ru', 'to_weekday_ru', 'from_weekday_en',
        'to_weekday_en',)
    list_filter = ('from_weekday_uz', 'to_weekday_uz')

    fieldsets = [
        (_('Ish Kunlari'), {
            'classes': [],

            'fields': (
                ('from_weekday_uz', 'to_weekday_uz'),
            ),
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ('from_weekday_ru', 'to_weekday_ru', 'from_weekday_en', 'to_weekday_en'),
        }),
    ]


@admin.register(Weekends)
class WeekendsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'week_uz', 'week_ru', 'week_en',)

    fieldsets = [
        (_('Dam Olish Kunlari'), {
            'classes': [],

            'fields': (
                ('week_uz',),
            ),
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ('week_ru', 'week_en',),
        }),
    ]


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ("id", "title", "description", "image_tag", "image", "video_image", "video_image_tag", "url")


@admin.register(ClinicMember)
class ClinicMemberAdmin(TranslationAdmin):
    list_display = ("id",
                    "last_name", "first_name", "middle_name", "description", "images_tag", "telegram_link",
                    "instagram_link",
                    "facebook_link",)
    list_filter = ("last_name", "first_name", "middle_name",)
    search_fields = ("last_name", "first_name",)


@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_display = ("id", "title", "short_description", "image_tag",)
    list_filter = ("id", "title",)
    search_fields = ("title",)
    group_fieldsets = True

    fieldsets = [
        ('Services', {
            'fields': [
                "title", "short_description", 'image',
            ],
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ("brand",),
        }),

    ]


@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    list_display = ("id", "title", "short_description", "image_tag", "price", "count")
    list_filter = ("id", "title")
    search_fields = ("title",)


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "phone", "email", "weekday", "weekends", "from_hour", "to_hour",)


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ("id", "last_name", "first_name", "phone", "message", 'product')
    list_filter = ("id", "last_name", "phone", "first_name",)
    search_fields = ("last_name", "first_name", "phone",)
    ordering = ("-id",)
