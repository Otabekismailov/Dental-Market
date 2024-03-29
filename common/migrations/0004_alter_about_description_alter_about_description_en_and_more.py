# Generated by Django 5.0.2 on 2024-03-05 13:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_partners_delete_services_alter_clinicmember_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='description_uz',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
