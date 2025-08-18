from django.contrib import admin
from django.urls import path

from mycontacts import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.show, name="home"),             
    path('add/', views.add), 
    path('delete/<int:contact_id>/', views.delete, name='delete'),
    path('editar/<int:contact_id>/', views.editar, name='editar'), 
]