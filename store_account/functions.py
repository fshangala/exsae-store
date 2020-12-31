from django.contrib.auth.models import User

def signup(data):
    user = User.objects.create(username=data["username"], email=data["email"], first_name=data["first_name"], last_name=data["last_name"])
    user.set_password(data=["password"])
    user.save()
    return True