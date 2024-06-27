from django.urls import path
from .views import DocumentUploadView, DocumentListView, ExtractedDataListView

urlpatterns = [
    path('documents/upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('documents/<int:document_id>/extracted-data/', ExtractedDataListView.as_view(), name='extracted-data-list'),
]
