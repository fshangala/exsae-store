from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=False)
    address_text = models.CharField(max_length=200, blank=True)
    address_geo = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    phone2 = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to="users", default="dashboard/img/find_user.png")
