from django.urls import path
from . import views

urlpatterns = [
    path('ciudad/<int:id>', views.map, name='map'),
    path('', views.default, name='default'),
]