from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


# class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
#
#     class Meta:
#         model = FileUpload
#         read_only_fields = ('created', 'datafile', 'owner')