from django.db import models

class Document(models.Model):
    DOCUMENT_TYPES = [
        ('2A', 'Type 2A'),
        ('2B', 'Type 2B'),
        ('3', 'Type 3'),
    ]

    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    document_type = models.CharField(max_length=2, choices=DOCUMENT_TYPES)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.uploaded_at}"

class ExtractedData(models.Model):
    document = models.ForeignKey(Document, related_name='extracted_data', on_delete=models.CASCADE)
    data_point = models.CharField(max_length=100)
    value = models.TextField()
    confidence = models.FloatField()

    def __str__(self):
        return f"{self.document} - {self.data_point}"