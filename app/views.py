from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse  
from django.http import JsonResponse
from .models import Component, Category, Document, Location, Package, Purchase, Supplier, StockMovement
from .forms import ComponentForm, CategoryForm, DocumentForm, LocationForm, PackageForm, PurchaseForm, SupplierForm, StockMovementForm
from django.http import HttpResponse

@csrf_exempt
def save_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors})

    return HttpResponse("Invalid request method", status=400)


class ComponentListView(ListView):
    model = Component
    template_name = '/home/n/Desktop/en/uygulama/app/templates/home.html'  # Değiştirilecek
    context_object_name = 'components'


def home(request):
    return render(request, '/home/n/Desktop/en/uygulama/app/templates/home.html')  # Değiştirilecek

def home(request):
    components = Component.objects.all()
    categories = Category.objects.all()
    documents = Document.objects.all()
    locations = Location.objects.all()
    packages = Package.objects.all()
    purchases = Purchase.objects.all()
    suppliers = Supplier.objects.all()
    stock_movements = StockMovement.objects.all()

    context = {
        'components': components,
        'categories': categories,
        'documents': documents,
        'locations': locations,
        'packages': packages,
        'purchases': purchases,
        'suppliers': suppliers,
        'stock_movements': stock_movements,
    }

    return render(request, 'home.html', context)
def save_component(request):
    # Bu fonksiyonun içeriğini buraya ekleyin
    pass

def delete_component(request, pk):
    # Bu fonksiyonun içeriğini buraya ekleyin
    pass


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