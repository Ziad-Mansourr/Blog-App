from django.db import models

from . import conf, managers, mixins


class Post(models.Model):
    user_name = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    status = models.CharField(max_length=50, choices=conf.StatusChoices.choices)
    published_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['published_at']
