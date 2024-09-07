# forms.py

from django import forms
from .models import File, Folder  # Ensure these models are correctly defined in models.py

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent_folder']
