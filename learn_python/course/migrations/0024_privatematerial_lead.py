# Generated by Django 4.1.7 on 2023-07-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_alter_privatematerial_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='privatematerial',
            name='lead',
            field=models.TextField(blank=True, max_length=250, null=True, verbose_name='Лид'),
        ),
    ]
