from rest_framework import serializers

from .models import ImageModel


class ImageModelSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ImageModel
        # fields = ('id', 'image', 'category', 'processed')
        fields = '__all__'
