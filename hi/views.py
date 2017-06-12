from .models import FileUpload
from .serializers import FileUploadSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser


class FileUploadView2(APIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer


class FileUploadView(APIView):
    # parser_classes = (MultiPartParser, FormParser)
    parser_classes = (FileUploadParser,)

    def put(self, request, format=None):

        file_obj = request.data['file']

        return Response(status=204)
