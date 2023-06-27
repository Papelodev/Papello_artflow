from django.contrib import admin
from apps.orders.models import Order, OrderProduct, Product


class OrderProductInline(admin.TabularInline):
   model = OrderProduct
   extra = 0
   fields = ('product', 'quantity', 'image')
   

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
   inlines = [OrderProductInline]
   list_display = ("formatted_date_order", "idOrder", "nameStatus", "order_total", "customer")
   list_display_links = ("idOrder", "formatted_date_order")

   def formatted_date_order(self, obj):
        if obj.dateOrder:
            return obj.dateOrder.strftime('%d/%m/%Y')
        return None

   formatted_date_order.short_description = 'Date Order'


  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   pass
