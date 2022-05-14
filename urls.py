from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('customer/', views.customer),
    path('upload_file/', views.upload_file),
    path('read_file/',views.read_file),
    path('product/',views.product),
    path('uploadproduct_file/', views.uploadproduct_file)
]
