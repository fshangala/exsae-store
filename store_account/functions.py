from django.contrib.auth.models import User

#User start
def get_user_by_id(user_id):
    user = User.objects.get(pk=user_id)
    obj = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "full_name": user.get_full_name()
    }
    return obj
#User end

def signup(data):
    user = User.objects.create(username=data["username"], email=data["email"], first_name=data["first_name"], last_name=data["last_name"])
    user.set_password(data=["password"])
    user.save()
    return True