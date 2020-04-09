from django.contrib import admin
from .models import UserOrder, OrderLineItem


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class UserOrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(UserOrder, UserOrderAdmin)
