# Generated by Django 4.0.3 on 2022-03-30 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_remove_service_region_service_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='subject',
        ),
    ]
