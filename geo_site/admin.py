from django.contrib import admin

from .models import Region, Country, LearnRate

admin.site.register(Region)
admin.site.register(Country)
admin.site.register(LearnRate)
