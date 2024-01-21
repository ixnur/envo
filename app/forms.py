# forms.py

from django import forms
from .models import DocumentType, Component, Category, Document, Location, Package, Document, Location, Package

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = '__all__'
