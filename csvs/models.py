from django.db import models

# Create your models here.

class Csv(models.Model):
    file_name=models.FileField(upload_to='csvs')
    uploaded=models.DateField(auto_now_add=True)
    activated=models.BooleanField(default=False)

    def __str__(self):
        return f"FIle id: {self.id}"
        
