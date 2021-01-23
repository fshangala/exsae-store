from django.contrib.auth.models import User
from .models import Profile

#User start
def get_user_by_id(user_id):
    user = User.objects.get(pk=user_id)
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = Profile(user=user)
        profile.save()
    obj = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "full_name": user.get_full_name(),
        "profile": {
            "is_seller": profile.is_seller,
            "picture": profile.picture.name,
            "address_text": profile.address_text,
            "phone": profile.phone,
            "phone2": profile.phone2,
        }
    }
    return obj
#User end