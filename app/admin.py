from django.contrib import admin
from .models import Category, Component, ComponentDocumentLink, Document, DocumentType, Location, LocationType, Manufacturer, Package, Purchase, PurchaseDetail, StockMovement

# Register your models here.
admin.site.register(Category)
admin.site.register(Component)
admin.site.register(ComponentDocumentLink)
admin.site.register(Document)
admin.site.register(DocumentType)
admin.site.register(Location)
admin.site.register(LocationType)
admin.site.register(Manufacturer)
admin.site.register(Package)