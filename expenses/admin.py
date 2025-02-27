from django.contrib import admin

from expenses.models import Expense


# Register your models here.
@admin.register(Expense)
class Expense(admin.ModelAdmin):
    list_display = ('amount', 'user', 'date')
    list_filter = ('amount', 'user', 'date')
    search_fields = ('amount', 'user', 'date')