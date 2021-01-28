from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from store_account.functions import get_user_by_id
from store_account.models import Profile
from store_products.models import Product, Brand
from store_products.forms import BrandForm, CategoryForm, ProductForm
from store_products.functions import get_brands_by_user, get_brand_by_id, get_products_by_brand, get_all_categories, get_product_by_id

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
        "user_brands": get_brands_by_user(request.user),
    }
    template = "dashboard/my_products.html"
    user_brands = get_brands_by_user(request.user)
    productList = []
    if user_brands:
        for brand in user_brands:
            temp_list = get_products_by_brand(Brand.objects.get(pk=brand["id"]))
            for p in temp_list:
                productList.append(p)

    context["user_products"] = productList
    print(productList)
    if request.method == "POST":
        data = dict(request.POST)
        if request.POST["type"] == "create_brand":
            data["user"] = request.user
            data["status"] = 'unapproved'
            data["name"] = data["name"][0]
            brandForm = BrandForm(data, request.FILES)
            if brandForm.is_valid():
                brandForm.save()
            else:
                return HttpResponse(brandForm.data)
        elif request.POST["type"] == "edit_brand":
            data["user"] = User.objects.get(username=data["user"][0])
            data["status"] = data["status"][0]
            data["name"] = data["name"][0]
            brandForm = BrandForm(data, request.FILES, instance=Brand.objects.get(pk=data["id"][0]))
            if brandForm.is_valid():
                brandForm.save()
            else:
                return HttpResponse("Failed to save")
    else:
        try:
            edit_brand = request.GET["edit-brand"]
        except:
            pass
        else:
            brand = get_brand_by_id(edit_brand)
            context["edit_brand"] = brand
    return render(request, template, context)

@login_required
def add_listing(request):
    context = {
        "user_brands": get_brands_by_user(request.user),
        "categories": get_all_categories(),
    }
    template = "dashboard/add-listing.html"
    if request.method == "POST":
        data = dict(request.POST)
        if request.POST["type"] == "add_listing":
            data["name"] = data["name"][0]
            data["description"] = data["description"][0]
            data["usual_price"] = data["usual_price"][0]
            data["listing_price"] = data["listing_price"][0]
            data["brand"] = data["brand"][0]
            data["category"] = data["category"][0]
            productForm = ProductForm(data)
            if productForm.is_valid():
                productForm.save()
                messages.success(request, "Product Successfully Added! Edit the product or skip.")
                return HttpResponseRedirect("/dashboard/edit-product/"+str(productForm.instance.id)+"/")
            else:
                messages.error(request, productForm.errors)
        else:
            messages.warning(request, "Nothing has been posted")
    
    return render(request, template, context)

@login_required
def edit_listing(request, product_id):
    context = {
        "user": get_user_by_id(request.user.id),
        "product": get_product_by_id(product_id)
    }
    template = "dashboard/edit-listing.html"
    return render(request, template, context)

@login_required
def categories(request):
    context = {
        "categories": get_all_categories(),
    }
    template = "dashboard/categories.html"
    if request.method == "POST":
        data = dict(request.POST)
        if request.POST["type"] == "create_category":
            data["status"] = "unapproved"
            data["name"] = data["name"][0]
            data["icon"] = data["icon"][0]
            form = CategoryForm(data)
            if form.is_valid():
                form.save()
                messages.success(request, "Category Successfully Created!")
                return HttpResponseRedirect(reverse("dashboard:categories"))
            else:
                print(form.errors)
                messages.error(request, form.errors)
    return render(request, template, context)