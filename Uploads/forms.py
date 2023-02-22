from django import forms

from .models import ExcelUpload

class ExcelUploadModelForm(forms.ModelForm):
    class Meta:
        model=ExcelUpload
        fields=('file_name',)
        
