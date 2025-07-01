from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from shop.models import Product, Customer, Category


def index(request: HttpRequest) -> HttpResponse:
    num_products = Product.objects.count()
    count_users = Customer.objects.count()
    count_categories = Category.objects.count()
    context = {
        "num_products": num_products,
        "count_users": count_users,
        "count_categories": count_categories,
    }
    return render(request, "home_page.html", context)
