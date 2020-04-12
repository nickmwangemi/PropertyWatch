from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ['agent','title']

admin.site.register(Listing,ListingAdmin)