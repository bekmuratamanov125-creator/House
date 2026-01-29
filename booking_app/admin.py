from django.contrib import admin
from .models import *

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    max_num = 10


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',  'city', 'region', 'price', 'is_active', 'type')
    list_filter = ('is_active', 'city', 'region', 'type')
    search_fields = ('title', 'description', 'address')
    inlines = [PropertyImageInline]



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('property', 'seller', 'rating', 'created_date')
    search_fields = ('property__title', 'buyer__username', 'comment')

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name',)
    search_fields = ('region_name',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name',)
    search_fields = ('city_name',)



