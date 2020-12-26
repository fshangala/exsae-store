from django.urls import path, include
from . import views

app_name="store"
urlpatterns = [
    path('', views.home, name="home"),
    path('contact-us/', views.contact, name="contact"),
]
