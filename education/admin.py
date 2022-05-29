from django.contrib import admin

from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'school',
        'education_level',
        'started_at', 'finished_at'
    ]
    list_display_links = 'id', 'school', 'education_level'
