from . import views
from django.urls import path, include
from .views import ComponentListView, save_component, delete_component

urlpatterns = [
    path('', views.home, name='home'),
    path('save_component/', save_component, name='save_component'),
    path('delete_component/<int:pk>/', delete_component, name='delete_component'),
]