# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Component, ComponentDocumentLink, Component, DocumentType, Document, Location, LocationType, Package, PurchaseDetail, Purchase, Supplier, StockMovement

from .forms import ComponentForm


def home(request):
    components = Component.objects.all()
    return render(request, 'templates/home.html', {'components': components})
 
"""
def component_list(request):
    components = Component.objects.all()
    return render(request, 'inventory/component_list.html', {'components': components})

def component_detail(request, slug):
    component = get_object_or_404(Component, slug=slug)
    return render(request, 'inventory/component_detail.html', {'component': component})

def add_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm()
    return render(request, 'inventory/add_component.html', {'form': form})

def edit_component(request, slug):
    component = get_object_or_404(Component, slug=slug)
    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            form.save()
            return redirect('component_list')
    else:
        form = ComponentForm(instance=component)
    return render(request, 'inventory/edit_component.html', {'form': form, 'component': component})

def delete_component(request, slug):
    component = get_object_or_404(Component, slug=slug)
    if request.method == 'POST':
        component.delete()
        return redirect('component_list')
    return render(request, 'inventory/delete_component.html', {'component': component})
"""