from django.shortcuts import render

from .models import HardSkill, SoftSkill


def skills_view(request):
    hard = HardSkill.objects.all()
    soft = SoftSkill.objects.all()
    return render(request, 'skills/pages/skills.html', {
        "hard": hard,
        "soft": soft,
    })
