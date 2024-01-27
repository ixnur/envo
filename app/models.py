from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import time
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ComponentDocumentLink(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Component(models.Model):
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_user_components(user):
        return Component.objects.filter(user=user)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('component_detail', args=[str(self.slug)])

class DocumentType(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Document(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=500, blank=True, null=True)
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    document_path = models.CharField(max_length=500)
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class LocationType(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Location(models.Model):
    name = models.CharField(max_length=100)
    location_type = models.ForeignKey('LocationType', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('Location', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Package(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PurchaseDetail(models.Model):
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Purchase(models.Model):
    date = models.DateField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class StockMovement(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    source_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='source_location')
    destination_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='destination_location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
