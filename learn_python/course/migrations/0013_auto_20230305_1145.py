# Generated by Django 3.2 on 2023-03-05 11:45

from django.db import migrations
import django.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_alter_course_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='theory',
            field=django.db.models.TextField(verbose_name='Теория'),
        ),
        migrations.AlterField(
            model_name='task',
            name='text',
            field=django.db.models.TextField(verbose_name='Текст задания'),
        ),
    ]
