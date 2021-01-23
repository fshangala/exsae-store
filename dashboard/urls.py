from django.urls import path
from . import views

app_name="dashboard"
urlpatterns = [
    path('', views.index, name="index"),
    path('my-products/', views.my_products, name="my-products"),
]
