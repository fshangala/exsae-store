from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'store/cart/index.html')

def checkout(request):
    return render(request, 'store/cart/checkout.html')

def wishlist(request):
    return render(request, 'store/cart/wishlist.html')