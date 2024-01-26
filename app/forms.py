from django import forms
from .models import Component

class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        fields = ['model', 'description', 'manufacturer', 'category', 'package', 'location', 'stock']
