from django.contrib import admin
from .models import product, cart, orders

# Register your models here.
class ProdAdmin(admin.ModelAdmin):
    list_display=['id','name','price','pdetails','cat','is_active']
    list_filter=('cat','is_active')
class cartAdmin(admin.ModelAdmin):
    list_display=['id','uid','pid']              
class orderAdmin(admin.ModelAdmin):
    list_display=['id','order_id','uid','pid']              
admin.site.register(cart, cartAdmin)
admin.site.register(product, ProdAdmin)
admin.site.register(orders, orderAdmin)