from django.contrib import admin
from .models import Station, Guestbook

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):

    list_display = ('order', 'title_ar', 'title_en') 
    ordering = ('order',)
    search_fields = ('title_ar', 'title_en')

@admin.register(Guestbook)
class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    ordering = ('-created_at',)
    list_filter = ('created_at', 'user')