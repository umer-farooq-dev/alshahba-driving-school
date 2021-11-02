# Generated by Django 3.2.6 on 2021-08-25 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
                ('feature_1', models.CharField(max_length=200)),
                ('feature_2', models.CharField(max_length=200)),
                ('feature_3', models.CharField(max_length=200)),
                ('feature_4', models.CharField(blank=True, max_length=200, null=True)),
                ('feature_5', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Packages',
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='WebsiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, max_length=200, null=True)),
                ('tagline', models.CharField(max_length=500)),
                ('physical_address', models.CharField(blank=True, max_length=1000, null=True)),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/logo')),
                ('youtube_video_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Website Information',
                'verbose_name_plural': 'Website Information',
            },
        ),
    ]