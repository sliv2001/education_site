"""
This module states all database tables accessible from admin panel.
"""
from django.contrib import admin

from .models import Region, Country, LearnRate

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(LearnRate)
