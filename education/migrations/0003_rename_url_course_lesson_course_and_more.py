# Generated by Django 5.0.2 on 2024-03-12 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='url_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='url_lesson',
            new_name='lesson',
        ),
    ]
