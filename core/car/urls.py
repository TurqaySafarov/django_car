from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('owner/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('add_car/', views.add_car, name='add_car'),
    path('add_owner/', views.add_owner, name='add_owner'),
]
