# Generated by Django 3.2 on 2023-03-05 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20230305_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lead',
            field=models.TextField(max_length=250, verbose_name='Лид'),
        ),
    ]