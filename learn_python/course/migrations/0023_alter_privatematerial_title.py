# Generated by Django 4.1.7 on 2023-07-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_rename_introduction_privatematerial_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privatematerial',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
