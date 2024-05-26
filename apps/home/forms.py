from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField(label='Select a PDF file', help_text='File must be in PDF format', widget=forms.FileInput(attrs={'accept': '.pdf'}))
