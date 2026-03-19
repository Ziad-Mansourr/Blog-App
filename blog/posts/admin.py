from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from . import models


@admin.register(models.Post)
class PostAdmin(ModelAdmin):
    model = models.Post
    list_display = ["id", "title", "published_at"]
    inlines = []
