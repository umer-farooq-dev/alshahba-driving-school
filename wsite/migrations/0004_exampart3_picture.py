# Generated by Django 3.2.6 on 2021-08-26 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wsite', '0003_exampart1_exampart2_exampart3'),
    ]

    operations = [
        migrations.AddField(
            model_name='exampart3',
            name='picture',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/question/'),
            preserve_default=False,
        ),
    ]
