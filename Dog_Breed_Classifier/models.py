import datetime

from django.db import models

from .file_validator import validate_file_extension


class ImageModel(models.Model):
    image = models.FileField(upload_to='uploads/%Y/%m/%d/',
                             validators=[validate_file_extension])
    category = models.CharField(max_length=50, default='Undefined')
    processed = models.BooleanField(default=False)
    upload_date = models.DateField(default=datetime.date.today)
    processing_time = models.CharField(max_length=15, default='0 secondes')
