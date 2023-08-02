from django.db import models


class Board(models.Model):
    embed = models.TextField(
        verbose_name='Код для вставки'
    )
    key = models.CharField(
        verbose_name='Ключ для подключения',
        max_length=128,
    )
