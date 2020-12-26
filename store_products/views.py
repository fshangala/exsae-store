from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/products/index.html')

def product_detail(request):
    return render(request, 'store/products/product-detail.html')