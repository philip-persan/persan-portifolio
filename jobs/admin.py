from django.contrib import admin

from .models import Experience


@admin.register(Experience)
class EducationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'enterprise',
        'position', 'is_on',
        'started_at', 'finished_at'
    ]
    list_display_links = 'id', 'enterprise', 'position'
