from django import forms
from .models import Component, Document, Manufacturer, Category, Package, Location, 
from django.contrib.auth.models import User
import hashlib



class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'








class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'content']

    def clean_content(self):
        content = self.cleaned_data['content']
        hash_object = hashlib.md5(content.read())
        hash_value = hash_object.hexdigest()
        existing_document = Document.objects.filter(hash_value=hash_value).first()
        if existing_document:
            return existing_document
        else:
            document = Document(name=self.cleaned_data['name'], content=content)
            document.hash_value = hash_value
            document.save()
            return document
        
