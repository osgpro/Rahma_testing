# Generated by Django 4.0.3 on 2022-03-30 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_mentalhealthprogramsoffered_program_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mentalhealthprogramsoffered',
            options={'verbose_name_plural': 'Mental Health Programs Offered'},
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.CharField(max_length=370),
        ),
    ]