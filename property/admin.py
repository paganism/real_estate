from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town_district','town', 'address',)
    readonly_fields = ["created_at",]

admin.site.register(Flat, FlatAdmin)
