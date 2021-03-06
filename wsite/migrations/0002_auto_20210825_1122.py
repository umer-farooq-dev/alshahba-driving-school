# Generated by Django 3.2.6 on 2021-08-25 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wsite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websiteinfo',
            name='tagline',
        ),
        migrations.AddField(
            model_name='websiteinfo',
            name='description',
            field=models.TextField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='websiteinfo',
            name='youtube_video_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
