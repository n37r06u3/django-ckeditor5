from django.db import models

from ckeditor5.fields import RichTextField

class ExampleNonUploadModel(models.Model):
    content = RichTextField()