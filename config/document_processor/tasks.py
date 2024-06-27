from celery import shared_task
from .services import pdf_ingestion, document_classification, anchor_detection, data_extraction
from apps.core.models import Document, ExtractedData

@shared_task
def process_document(document_id):
    document = Document.objects.get(id=document_id)
    pages = pdf_ingestion.ingest_pdf(document.file.path)
    
    for i, page in enumerate(pages):
        doc_type = document_classification.classify_document(page)
        if i == 0:  # Only set document type based on first page
            document.document_type = doc_type
            document.save()
        
        anchors = anchor_detection.detect_anchors(page)
        extracted_data = data_extraction.extract_data(page, anchors)
        
        for key, value in extracted_data.items():
            ExtractedData.objects.create(
                document=document,
                data_point=key,
                value=value,
                confidence=0.95  # Placeholder confidence value
            )
    
    document.processed = True
    document.save()