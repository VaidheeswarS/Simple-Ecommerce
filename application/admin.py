from django.contrib import admin
from .models import Seller_reg,products,consumer,buyer

# Register your models here.

admin.site.register(consumer)
admin.site.register(products)
admin.site.register(Seller_reg)
admin.site.register(buyer)