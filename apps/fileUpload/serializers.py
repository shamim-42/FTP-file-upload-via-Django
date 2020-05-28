from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
  # name = serializers.CharField("max_length")
  file = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
  type = serializers.CharField(max_length=200)