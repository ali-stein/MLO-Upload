from django.contrib import admin
from .models import EventLocation
from .models import calUser
from .models import Event

#admin.site.register(EventLocation)
admin.site.register(calUser)
#admin.site.register(Event)

@admin.register(EventLocation)
class EventLocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    ordering = ('name',)
    search_fields = ('name,', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'event_location'), 'event_date', 'attendees', 'description')
    list_display = ('name', 'event_date', 'event_location')
    list_filter = ('event_date', 'event_location')
    ordering = ('event_date',)
