from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]
