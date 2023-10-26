from rest_framework import serializers
from .models import UploadImage,FileUpload

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = '__all__'
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = '__all__'