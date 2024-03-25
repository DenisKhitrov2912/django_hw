from django.contrib import admin

from users.models import User#, ContManager


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'phone', 'country',)
    list_filter = ('email', 'country',)
    search_fields = ('email', 'country',)


# @admin.register(ContManager)
# class ContManagerAdmin(admin.ModelAdmin):
#     list_display = ('email', 'avatar', 'phone', 'country',)
#     list_filter = ('email', 'country',)
#     search_fields = ('email', 'country',)
