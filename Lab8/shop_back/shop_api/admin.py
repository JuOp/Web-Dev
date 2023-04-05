from django.contrib import admin
from shop_api.models import Product, Category

admin.site.register((Product, Category))

# Register your models here.
