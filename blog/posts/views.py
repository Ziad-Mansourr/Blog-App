from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from . import conf, filters, models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_class = filters.PostFilter
    parser_classes = [MultiPartParser, FormParser]
    search_fields = ["user_name", "title", "description"]
    ordering_fields = ["published_at", "created_at"]
