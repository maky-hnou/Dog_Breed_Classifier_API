from rest_framework import viewsets

from .models import ImageModel
from .serializers import ImageModelSerializer


class ImageModelViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
