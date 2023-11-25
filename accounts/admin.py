from django.contrib import admin
from .models import UserProfile,ShoppingList
from django.utils.html import format_html


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    # def thumbnail(self, object):
    #     return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
    # thumbnail.short_description = 'Profile Picture'
    list_display = ( 'user', 'city', 'state', 'country')

class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('list_item','created_date')

admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(UserProfile, UserProfileAdmin)