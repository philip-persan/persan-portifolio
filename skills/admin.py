from django.contrib import admin

from .models import HardSkill, SoftSkill


@admin.register(SoftSkill)
class SoftSkillAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',
    ]
    list_display_links = 'id', 'name'


@admin.register(HardSkill)
class HardSkillAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name',
    ]
    list_display_links = 'id', 'name'
