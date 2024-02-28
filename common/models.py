from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify, gettext_lazy as _

WEEKDAYS_EN = (
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Friday")),
    (6, _("Saturday")),
    (7, _("Sunday")),
)

WEEKDAYS_RU = (
    (1, _("Понедельник")),
    (2, _("Вторник")),
    (3, _("Среда")),
    (4, _("Четверг")),
    (5, _("Пятница")),
    (6, _("Суббота")),
    (7, _("Воскресенье")),
)

WEEKDAYS_UZ = (
    (1, _("Dushanba")),
    (2, _("Seshanba")),
    (3, _("Chorshanba")),
    (4, _("Payshanba")),
    (5, _("Juma")),
    (6, _("Shanba")),
    (7, _("Yaxshanba")),
)


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class About(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    video_image = models.ImageField(upload_to='about/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    telegram_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('-id',)
        verbose_name_plural = "Clinic Haqida Ma'lumot"
        verbose_name = "Clinic Haqida Ma'lumot"

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'

    def video_image_tag(self):
        if self.video_image:
            return mark_safe(
                f'<a href="{self.video_image.url}"><img src="{self.video_image.url}" style="height:40px;"/></a>')
        return 'no_image'


class ClinicMember(BaseModel):
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Familiya')
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Ism")
    middle_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Otasini Ism")
    description = models.TextField(null=True, blank=True, verbose_name="O'zi Xaqida Ma'lumot")
    image = models.ImageField(upload_to='members/', null=True, blank=True)
    telegram_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.last_name

    def images_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'


class Services(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='services/', null=True, blank=True)
    # Buni so'rash Kerak !!
    brand = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'

    class Meta:
        verbose_name_plural = 'Ishlab chiqaruvchilar'
        verbose_name = 'Ishlab chiqaruvchilar'


class Products(BaseModel):
    title = models.CharField(max_length=255, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    price = models.DecimalField(max_digits=9999999, decimal_places=0, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'

    class Meta:
        verbose_name_plural = 'Mahsulotlar'
        verbose_name = 'Mahsulotlar'


class ProductImages(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='product_images',
                                verbose_name="Mahsulot rasmlari")
    images = models.ImageField(upload_to='product/', null=True, blank=True)

    def __str__(self):
        if self.images:
            return self.images.url
        return 'non_file'

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'


class Weekdays(BaseModel):
    from_weekday_uz = models.IntegerField(choices=WEEKDAYS_UZ, verbose_name="Qaysi haftadan")
    to_weekday_uz = models.IntegerField(choices=WEEKDAYS_UZ, verbose_name="Qaysi Haftagacha")
    from_weekday_en = models.IntegerField(choices=WEEKDAYS_EN, blank=True, null=True, verbose_name='From which week')
    to_weekday_en = models.IntegerField(choices=WEEKDAYS_EN, blank=True, null=True, verbose_name='Until what week')
    from_weekday_ru = models.IntegerField(choices=WEEKDAYS_RU, blank=True, null=True, verbose_name='C какой недели')
    to_weekday_ru = models.IntegerField(choices=WEEKDAYS_RU, blank=True, null=True, verbose_name="До какой недели")

    class Meta:
        verbose_name = 'Ish Kunlari'
        verbose_name_plural = 'Ish Kunlari'

    def __str__(self):
        return f'{self.from_weekday_en} - {self.to_weekday_en}'

    def save(self, *args, **kwargs):
        if self.from_weekday_uz and self.to_weekday_uz:
            self.from_weekday_ru = self.from_weekday_uz
            self.from_weekday_en = self.from_weekday_uz
            self.to_weekday_ru = self.to_weekday_uz
            self.to_weekday_en = self.to_weekday_uz
        super(Weekdays, self).save(*args, **kwargs)


class Weekends(BaseModel):
    week_uz = models.IntegerField(choices=WEEKDAYS_UZ, verbose_name="Qaysi Hafta Kunni")
    week_ru = models.IntegerField(choices=WEEKDAYS_RU, null=True, blank=True, verbose_name='Какой день недели')
    week_en = models.IntegerField(choices=WEEKDAYS_EN, null=True, blank=True, verbose_name='What day of the week')

    class Meta:
        verbose_name = 'Dam Olish Kunlari'
        verbose_name_plural = 'Dam Olish Kunlari'

    def __str__(self):
        return f'{self.week_uz}'

    def save(self, *args, **kwargs):
        if self.week_uz:
            self.week_en = self.week_uz
            self.week_ru = self.week_uz

        super(Weekends, self).save(*args, **kwargs)


class Contacts(BaseModel):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    weekday = models.ForeignKey(Weekdays, on_delete=models.SET_NULL, null=True, related_name='contacts', blank=True,
                                verbose_name='Ish Kunlari')
    weekends = models.ForeignKey(Weekends, on_delete=models.SET_NULL, null=True, verbose_name='Dam Olish Kunlari',
                                 related_name='contacts_not', blank=True)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Kontraklar'
        verbose_name = 'Kontraklar'
        unique_together = ('from_hour', 'to_hour')


class ApplicationForm(BaseModel):
    full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name='form_product', blank=True)

    class Meta:
        verbose_name_plural = 'Xabar'
        verbose_name = 'Xabar'


class Testimonial(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class TestimonialUser(BaseModel):
    full_name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='testimonial/', null=True, blank=True)
    testimonial = models.ForeignKey(Testimonial, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name

    def image_tag(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}"><img src="{self.image.url}" style="height:40px;"/></a>')
        return 'no_image'


class Banners(BaseModel):
    title = models.CharField(max_length=255)
    short_description = models.TextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to='banners/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='banners/', null=True, blank=True)

    def __str__(self):
        return self.title

    def image_tag_1(self):
        if self.image_1:
            return mark_safe(f'<a href="{self.image_1.url}"><img src="{self.image_1.url}" style="height:40px;"/></a>')
        return 'no_image'

    def image_tag_2(self):
        if self.image_2:
            return mark_safe(f'<a href="{self.image_2.url}"><img src="{self.image_2.url}" style="height:40px;"/></a>')
        return 'no_image'
