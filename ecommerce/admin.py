from django.contrib import admin
from .models import Product, Order, Review, Address
from ecommerce.models import CustomUser
from django.contrib.admin.models import CustomLogEntry
from .models import CustomLogEntry 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Customize the Product admin here
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at',)

@admin.register(CustomUser)  # Change User to CustomUser
class UserAdmin(admin.ModelAdmin):
    # Customize the User admin here
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Customize the Order admin here
    list_display = ('user', 'order_date', 'status', 'total_price')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email')
    ordering = ('-order_date',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # Customize the Review admin here
    list_display = ('product', 'user', 'created_at', 'rating')
    list_filter = ('product',)
    search_fields = ('user__username', 'user__email', 'product__name')
    ordering = ('-created_at',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    # Customize the Address admin here
    list_display = ('user', 'street', 'city', 'state', 'postal_code', 'is_billing_address')
    list_filter = ('is_billing_address',)
    search_fields = ('user__username', 'user__email', 'street', 'city', 'state', 'postal_code')

@admin.register(CustomLogEntry)  # Use the renamed CustomLogEntry model
class CustomLogEntryAdmin(admin.ModelAdmin):-