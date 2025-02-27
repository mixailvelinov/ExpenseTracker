from django.contrib import admin

from accounts.models import CustomUser, Profile


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth')
    list_filter = ('username', 'email', 'first_name', 'last_name', 'date_of_birth')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    def get_user_username(self, obj):
        return obj.user.username

    list_display = ('get_user_username', 'occupation', 'interests')
    search_fields = ('occupation', 'interests')
    list_filter = ('occupation', 'interests')

