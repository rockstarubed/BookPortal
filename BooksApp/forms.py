from django import forms
from . models import Books


# Uploadform based on Model fields
class UploadForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('bookname', 'bookauthor','document')