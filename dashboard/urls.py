from django.urls import path
from . import views

app_name="dashboard"
urlpatterns = [
    path('', views.index, name="index"),
    path('my-products/', views.my_products, name="my-products"),
    path('add-listing/', views.add_listing, name="add-listing"),
    path('edit-listing/<product_id>/', views.edit_listing, name="edit-listing"),
    path('categories/', views.categories, name="categories"),
]
