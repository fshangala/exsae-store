from django.urls import path
from . import views

app_name="account"
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('forgot-password/', views.forgot_password, name="forgot-password"),
]
