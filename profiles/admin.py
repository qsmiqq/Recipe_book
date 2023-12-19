from django.contrib import admin
from .models import Profile
from django.utils.safestring import mark_safe


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Registration of model Profiles in the admin panel"""
    list_display = ('id', 'email')