from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatOwnershipInline(admin.TabularInline):
    model = Flat.flats_owners.through
    raw_id_fields = ('flat', 'owner',)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town_district','town', 'address',)
    readonly_fields = ['created_at',]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number',)
    raw_id_fields = ('who_liked',)
    inlines = [FlatOwnershipInline]

admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ('complained_user','complained_flat',)
    raw_id_fields = ('complained_flat', 'complained_user',)
    
admin.site.register(Complaint, ComplaintAdmin)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone',)
    
admin.site.register(Owner, OwnerAdmin)
