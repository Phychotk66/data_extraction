from rest_framework import serializers
from apps.core.models import Document, ExtractedData

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'file', 'uploaded_at', 'document_type', 'processed']
        read_only_fields = ['uploaded_at', 'document_type', 'processed']

class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = ['id', 'document', 'data_point', 'value', 'confidence']