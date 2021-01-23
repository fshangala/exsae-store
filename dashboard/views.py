from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store_account.functions import get_user_by_id
from store_account.models import Profile

# Create your views here.
@login_required
def index(request):
    if request.method == "POST":
        if request.POST["type"] == "become_seller":
            try:
                profile = Profile.objects.get(user=request.user)
            except:
                profile = Profile(user=request.user)
                profile.save()
            profile.address_text = request.POST["address_text"]
            profile.phone = request.POST["phone"]
            profile.phone2 = request.POST["phone2"]
            profile.is_seller = True
            profile.save()
            messages.success(request, "Your request has been approved.")
            
    user = get_user_by_id(request.user.id)
    context = {
        "user": user,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def my_products(request):
    context = {
        "user": get_user_by_id(request.user.id),
    }
    template = "dashboard/my_products.html"
    return render(request, template, context)