# Generated by Django 4.1.7 on 2023-08-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0024_privatematerial_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatematerial',
            name='lead',
            field=models.TextField(blank=True, default='', max_length=250, verbose_name='Лид'),
        ),
    ]
