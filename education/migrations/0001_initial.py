# Generated by Django 5.0.2 on 2024-02-27 18:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_course', models.CharField(max_length=50, verbose_name='название курса')),
                ('image_course', models.ImageField(blank='True', null='True', upload_to='course/', verbose_name='картинка курса')),
                ('description_course', models.TextField(verbose_name='описание курса')),
                ('author', models.ForeignKey(blank='True', null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
