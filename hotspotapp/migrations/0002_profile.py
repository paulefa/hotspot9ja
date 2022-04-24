# Generated by Django 3.2.13 on 2022-04-24 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotspotapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('about', models.CharField(max_length=400)),
                ('company', models.CharField(max_length=200)),
                ('job', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(max_length=300)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('twitter_url', models.URLField()),
                ('facebook_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('linkedin_url', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
