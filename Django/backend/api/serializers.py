from api.models import DataFire
from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class DataFireSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataFire
        fields = '__all__'
