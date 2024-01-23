from django import forms
from .models import Category, ComponentDocumentLink, Component, DocumentType, Document, Location, LocationType, Package, PurchaseDetail, Purchase, Supplier, StockMovement

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = '__all__'
        exclude = ['document_links']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'package': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Name',
            'description': 'Description',
            'category': 'Category',
            'supplier': 'Supplier',
            'location': 'Location',
            'package': 'Package',
        }
        help_texts = {
            'name': 'Enter the name of the component.',
            'description': 'Enter a description of the component.',
            'category': 'Select a category for the component.',
            'supplier': 'Select a supplier for the component.',
            'location': 'Select a location for the component.',
        }

class ComponentDocumentLinkForm(forms.ModelForm):
    class Meta:
        model = ComponentDocumentLink
        fields = '__all__'

class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = LocationType
        fields = '__all__'

class PurchaseDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetail
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
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
