from django.contrib import admin
from users import models


@admin.register(models.Board)
class BoardAdmin(admin.ModelAdmin):
    pass
