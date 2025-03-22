from django.contrib import admin


from common.models import Weekdays, Weekends, About, ClinicMember, Partners, Products, Contacts, ApplicationForm, \
    WEEKDAYS_UZ, Testimonial, TestimonialUser, Banners, ProductImages, Category
from django.utils.text import slugify, gettext_lazy as _
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from adminsortable2.admin import SortableAdminMixin


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
    list_display = (
        "id", "title", "description", "image_tag", "image", "video_image", "video_image_tag", "url", "telegram_link",
        "instagram_link", "facebook_link", "youtube_link")
    fieldsets = [
        ('About', {
            'fields': [
                "title", "description", 'image', "url",
                "telegram_link", "instagram_link", "facebook_link", "youtube_link"],
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ("video_image",),
        }),

    ]
    group_fieldsets = True


@admin.register(ClinicMember)
class ClinicMemberAdmin(TranslationAdmin):
    list_display = ("id",
                    "last_name", "first_name", "middle_name", "description", "images_tag",)
    list_filter = ("last_name", "first_name", "middle_name",)
    search_fields = ("last_name", "first_name",)
    group_fieldsets = True

    fieldsets = [
        (_('Mutaxasislar'), {
            'classes': [],

            'fields': (
                ("last_name", "first_name", "middle_name", "description", "image"),
            ),
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ('telegram_link', 'instagram_link', 'facebook_link',),
        }),
    ]


@admin.register(Partners)
class PartnersAdmin(TranslationAdmin):
    list_display = ("id", "title", "short_description", "image_tag", "partner_url",)
    list_filter = ("id", "title", "partner_url",)
    search_fields = ("title",)
    group_fieldsets = True

    fieldsets = [
        ('Partners', {
            'fields': [
                "title", "short_description", 'image', "partner_url",
            ],
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ("brand",),
        }),

    ]


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin,TranslationAdmin):
    list_display = ("id", "name", "image_tag", "my_order")
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("my_order",)
    sortable_by = ()


class ProductImageAdmin(admin.StackedInline):
    model = ProductImages
    extra = 1


@admin.register(Products)
class ProductsAdmin(TranslationAdmin):
    list_display = ("id", "title", "short_description", "image_tag", "price", "count", "category")
    list_filter = ("id", "title", "category")
    search_fields = ("title",)
    inlines = [ProductImageAdmin]


@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "phone", "email", "weekday_day", "weekends_day", "from_hour", "to_hour",)

    def weekday_day(self, obj):
        f = ''
        t = ''
        data = obj.weekday
        if data:
            for k, v in WEEKDAYS_UZ:

                if k == data.from_weekday_uz:
                    f += v
                if k == data.to_weekday_uz:
                    t += v
            return f'{f} - {t}'
        else:
            return 'no_data'

    def weekends_day(self, obj):
        f = ''
        data = obj.weekends
        if data:
            for k, v in WEEKDAYS_UZ:
                if k == data.week_uz:
                    f += v

            return f'{f}'

        else:
            return 'no_data'


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "message", 'category')
    list_filter = ("id", "full_name", "phone",)
    search_fields = ("full_name", "phone",)
    ordering = ("-id",)


@admin.register(TestimonialUser)
class TestimonialUserAdmin(TranslationAdmin):
    list_display = ("id", "full_name", "description", "image_tag", 'image')


class TestimonialUserStackedInline(TranslationStackedInline):
    model = TestimonialUser
    extra = 1


@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    list_display = ("id", "title", "description",)
    actions = ['make_published']
    inlines = [TestimonialUserStackedInline]

    group_fieldsets = True


@admin.register(Banners)
class BannersAdmin(TranslationAdmin):
    list_display = ("id", "title", "short_description", 'image_tag_1', 'image_tag_2',)
    fieldsets = [
        ('Banners', {
            'fields': [
                "title", "short_description", 'image_1',
            ],
        }),
        (None, {
            'classes': ['empty-form'],
            'fields': ("image_2",),
        }),

    ]
    group_fieldsets = True
