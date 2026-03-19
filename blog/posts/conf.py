from django.db import models


class StatusChoices(models.TextChoices):
    PUBLISHED = "published", "Published"
    DRAFT = "draft", "Draft"
