from django.urls import path
from . import views

app_name="store_products"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/', views.product_detail, name="product-detail"),
]
