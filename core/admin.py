from django.contrib import admin
from .models import Event, Contact

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime')
    list_filter = ('datetime',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'organisation', 'phone')