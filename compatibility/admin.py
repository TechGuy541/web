from django.contrib import admin
from .models import GameEntry

# Register your models here.
class GameEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'published', 'game_id', 'compatibility', 'device_memory', 'created_at', 'updated_at')
    list_filter = ('compatibility', 'device_memory', 'published', 'created_at', 'updated_at')
    search_fields = ('name', 'game_id', 'compatibility', 'created_at', 'updated_at')
    ordering = ('compatibility', 'created_at', 'updated_at')

admin.site.register(GameEntry, GameEntryAdmin)