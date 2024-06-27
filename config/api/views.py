from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import DocumentSerializer, ExtractedDataSerializer
from apps.core.models import Document, ExtractedData
from apps.document_processor.tasks import process_document

class DocumentUploadView(generics.CreateAPIView):
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        document = serializer.save()
        process_document.delay(document.id)

class DocumentListView(generics.ListAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ExtractedDataListView(generics.ListAPIView):
    serializer_class = ExtractedDataSerializer

    def get_queryset(self):
        document_id = self.kwargs['document_id']
        return ExtractedData.objects.filter(document_id=document_id)