# Generated by Django 4.1.7 on 2023-07-31 16:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0020_course_access_course_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('introduction', models.TextField(verbose_name='Текст')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('access', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователи с доступом к материалу')),
            ],
            options={
                'verbose_name': 'приватный материал',
                'verbose_name_plural': 'приватные материалы',
            },
        ),
    ]