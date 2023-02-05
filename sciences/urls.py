from django.urls import path
from . import views

# systems runs through until they find the correct view
urlpatterns = [
    path('', views.science, name='science'),
    path('physics/', views.physics, name='physics'),
    path('chemistry/', views.chemistry, name='chemistry'),
]