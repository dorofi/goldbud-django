from django.contrib import admin
from .models import Order, OrderPhoto

class OrderPhotoInline(admin.TabularInline):
    model = OrderPhoto
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address", "created_at")
    search_fields = ("name", "phone", "address")
    inlines = [OrderPhotoInline]

@admin.register(OrderPhoto)
class OrderPhotoAdmin(admin.ModelAdmin):
    list_display = ("order", "image")
