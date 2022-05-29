from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Owner


@admin.register(Owner)
class EducationAdmin(auth_admin.UserAdmin):
    model = Owner
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Informações do Usuário", {"fields": (
            "profession", "degree", "location",
            "phone", "freelance", "open_to_work",
            "birthday"
        )}),
    )
