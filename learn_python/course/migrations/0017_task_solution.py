# Generated by Django 4.1.7 on 2023-05-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_example_is_published_task_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='solution',
            field=models.TextField(blank=True, null=True, verbose_name='Решение автора'),
        ),
    ]
