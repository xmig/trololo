from rest_framework.generics import RetrieveAPIView
from taggit.models import Tag
from projects.serializers import TagSerializer


class RetrieveTagView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer