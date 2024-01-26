from django.urls import path
from .views import home, component_list, component_detail, component_edit, component_delete, component_new

urlpatterns = [
    path('', home, name='home'),
    path('components/', component_list, name='component_list'),
    path('component/<slug:slug>/', component_detail, name='component_detail'),
    path('component/<slug:slug>/edit/', component_edit, name='component_edit'),
    path('component/<slug:slug>/delete/', component_delete, name='component_delete'),
    path('component/new/', component_new, name='component_new'),
]
