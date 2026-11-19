from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import Address, User
from catalog.models import Product, Category


# Register your models here.

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0
    fields = ['recipient_name', 'line_1', 'line_2', 'city', 'state', 'phone_number', 'is_default']


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'is_active']
    search_fields = ['email', 'username' ]
    fieldsets = BaseUserAdmin.add_fieldsets +(("Contact", {'fields': ('phone_number',)}),)
    addFieldsets = BaseUserAdmin.add_fieldsets + (("Contact", {'fields': ('phone_number', 'first_name', 'last_name', 'email',)}),)

    inlines = [AddressInline]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'recipient_name', 'line_1', 'line_2', 'city', 'state', 'phone_number', 'is_default']
    list_filter = ['state', 'city', 'is_default']
    search_fields = ['state', 'recipient_name', 'phone_number']
    autocomplete_fields  = ['user']
    list_select_related = ['user']






