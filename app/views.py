from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Component
from .forms import ComponentForm

class ComponentListView(ListView):
    model = Component
    template_name = '/home/n/Desktop/en/uygulama/app/templates/home.html'  # Değiştirilecek: Template adınıza göre güncelleyin
    context_object_name = 'components'

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

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def home(request):
    return render(request, '/home/n/Desktop/en/uygulama/app/templates/home.html')  # Değiştirilecek: Template adınıza göre güncelleyin


"""
def home(request):
    category = Category.objects.all()
    components = Component.objects.all()
    componentsdocumentlink = ComponentDocumentLink.objects.all()
    document = Document.objects.all()
    documenttype = DocumentType.objects.all()
    location = Location.objects.all()
    locationtype = LocationType.objects.all()
    package = Package.objects.all()
    purchasedetail = PurchaseDetail.objects.all()
    purchase = Purchase.objects.all()
    supplier = Supplier.objects.all()
    stockmovement = StockMovement.objects.all()

    context = {
        'category': category,
        'components': components,
        'componentsdocumentlink': componentsdocumentlink,
        'document': document,
        'documenttype': documenttype,
        'location': location,
        'locationtype': locationtype,
        'package': package,
        'purchasedetail': purchasedetail,
        'purchase': purchase,
        'supplier': supplier,
        'stockmovement': stockmovement,
    }

    return render(request, 'templates/home.html', {'components': components})
""" 
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