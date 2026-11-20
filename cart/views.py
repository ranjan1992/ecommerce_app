from django.shortcuts import render
from django.http import JsonResponse


def cart_add(request):
    print("Add to Cart button clicked")
    return JsonResponse({"message": "Add to Cart Button clicked !"})
