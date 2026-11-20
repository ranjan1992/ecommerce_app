from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import JsonResponse
from myapp.models import Product
from .cart import Cart


def cart_add(request):
    if request.method == "POST":
        cart = Cart(request)

        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)

    return JsonResponse({"message": "Add to Cart Button clicked !"})
