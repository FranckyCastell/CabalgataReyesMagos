from django.contrib import admin
from .models import Cities, Event

# Register your models here.


class CitiesAdmin(admin.ModelAdmin):
    list_display = ['name']  # COL DATA
    search_fields = ['name']  # SEARCH DATA


class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'end']  # COL DATA
    search_fields = ['title']  # SEARCH DATA


admin.site.register(Cities, CitiesAdmin)

admin.site.register(Event, EventAdmin)
