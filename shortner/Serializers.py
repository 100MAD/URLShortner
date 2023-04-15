from rest_framework.serializers import ModelSerializer

from .Models import ShortURL


class URLSerializer(ModelSerializer):

    class Meta:
        model = ShortURL
        fields = ['url', 'new_url','created_at']