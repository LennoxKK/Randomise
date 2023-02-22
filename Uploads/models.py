from django.db import models

# Create your models here.

class ExcelUpload(models.Model):
    file_name=models.FileField(upload_to='excel-uploads')
    uploaded=models.DateField(auto_now_add=True)
    activated=models.BooleanField(default=False)

    def __str__(self):
        return f"FIle id: {self.id}"
        
