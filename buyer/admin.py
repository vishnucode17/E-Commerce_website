from django.contrib import admin
from .models import Order
# Register your models here.
class OrderAdmin(admin.ModelAdmin): 
    list_display = ('product_name_buy', 'full_name', 'buy_date') 
  
    def active(self, obj): 
        return obj.is_active == 1
  
    active.boolean = True
  
admin.site.register(Order, OrderAdmin) 