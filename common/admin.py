from django.contrib import admin

from common.models import Wish


# Register your models here.
@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'price', 'is_bought', 'date_added')
    list_filter = ('title', 'price', 'is_bought', 'date_added', 'user')
    search_fields = ('title', 'price', 'is_bought', 'date_added', 'user')