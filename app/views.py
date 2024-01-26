from django.shortcuts import render, get_object_or_404, redirect
from .models import Component
from .forms import ComponentForm

def component_list(request):
    components = Component.objects.all()
    return render(request, 'inventory/component_list.html', {'components': components})

def component_detail(request, slug):
    component = get_object_or_404(Component, slug=slug)
    return render(request, 'inventory/component_detail.html', {'component': component})

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
    return render(request, 'inventory/component_edit.html', {'form': form})

def component_delete(request, slug):
    component = get_object_or_404(Component, slug=slug)
    component.delete()
    return redirect('component_list')

def component_new(request):
    if request.method == "POST":
        form = ComponentForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return redirect('component_detail', slug=component.slug)
    else:
        form = ComponentForm()
    return render(request, 'inventory/component_edit.html', {'form': form})
