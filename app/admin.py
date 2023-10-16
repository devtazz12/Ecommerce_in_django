from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(category)
admin.site.register(subcategory)

class productAdmin(admin.ModelAdmin):
    list_display=['name','subcategory','price','slug']
admin.site.register(product, productAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display=['user','prod','order_date_time', 'quantity', 'size']
admin.site.register(cart, cartAdmin)

admin.site.register(profile)
admin.site.register(Order)








