from django.contrib import admin

from .models import Flat

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner','town', 'address',)
    readonly_fields = ["construction_year",]

admin.site.register(Flat, FlatAdmin)
