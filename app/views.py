from django.db.models import OrderBy
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ComponentForm
from simple_history.models import HistoricalRecords
from .models import Category, Component, Document, ComponentDocumentLink, Document, ComponentDocumentLink, DocumentType, LocationType, Location, Manufacturer, Purchase, PurchaseDetail, Supplier, StockMovement    #history ekliyorum

def history_view(request):
    return render(request, 'history_view.html')

def home(request):
    return render(request, 'home.html')

def history_view(request):
    category_history = HistoricalRecords.objects.all().order_by('-history_date')
    component_history = HistoricalRecords.objects.all().order_by('-history_date')
    component_document_link_history = HistoricalRecords..objects.all().order_by('-history_date') 
    document_history = HistoricalRecords.objects.all().order_by('-history_date')
    document_type_history = HistoricalRecords..objects.all().order_by('-history_date')
    location_history = HistoricalRecords.objects.all().order_by('-history_date')
    location_type_history = HistoricalRecords..objects.all().order_by('-history_date')
    package_history = HistoricalRecords..objects.all().order_by('-history_date')
    purchase_history = HistoricalRecords..objects.all().order_by('-history_date')
    purchase_detail_history = HistoricalRecords..objects.all().order_by('-history_date')
    supplier_history = HistoricalRecords..objects.all().order_by('-history_date')
    stock_movement_history = HistoricalRecords..objects.all().order_by('-history_date')
    
    return render(request, 'history_view.html', {'component_history': component_history, 'document_history': document_history})

def component_list(request):
    components = Component.objects.all()
    return render(request, 'component_list.html', {'components': components})

def component_detail(request, slug):
    component = get_object_or_404(Component, slug=slug)
    return render(request, 'component_detail.html', {'component': component})

def component_edit(request, slug):
    component = get_object_or_404(Component, slug=slug)
    if request.method == "POST":
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return redirect('component_detail', slug=component.slug)
    else:
        form = ComponentForm(instance=component)
    return render(request, 'component_edit.html', {'form': form})

def component_delete(request, slug):
    component = get_object_or_404(Component, slug=slug)
    component.delete()
    return redirect('component_list')

def component_new(request):
    if request.method == "POST":
        component_new = Document.objects.filter(hash_value=component_new.hash_value).first()
        form = ComponentForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return redirect('component_detail', slug=component.slug)
    else:
        form = ComponentForm()
    return render(request, 'component_edit.html', {'form': form})
