from django.shortcuts import render
from django.http import JsonResponse


def cart_add(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        print("Product added to Cart's ID : ", product_id)
        print("Product added to Cart's Quantity : ", product_quantity)
    return JsonResponse({"message": "Add to Cart Button clicked !"})
