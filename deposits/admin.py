from django.contrib import admin

from deposits.models import Deposit


# Register your models here.
@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('amount', 'user', 'date')
    list_filter = ('amount', 'user', 'date')
    search_fields = ('amount', 'user', 'date')