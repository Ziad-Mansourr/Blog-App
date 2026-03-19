from rest_framework import serializers

from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = [
            "id",
            "user_name",
            "title",
            "description",
            "image",
            "status",
            "published_at",
            "created_at",
            "updated_at",
        ]
