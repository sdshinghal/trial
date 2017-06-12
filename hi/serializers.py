from rest_framework import serializers
from .models import FileUpload


# class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = FileUpload
#         read_only_fields = ('created', 'datafile', 'owner')


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = '__all__'
