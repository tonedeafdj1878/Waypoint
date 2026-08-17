from django.contrib import admin
from .models import Trail

@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    list_display = ('name', 'distance_km', 'elevation_gain_m', 'difficulty', 'created_at')
    search_fields = ('name', 'difficulty')