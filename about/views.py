from django.shortcuts import render
from education.models import Education
from jobs.models import Experience
from users.models import Owner


def about_view(request):
    user = Owner.objects.all().first()
    edus = Education.objects.all()
    jobs = Experience.objects.all()
    last_job = Experience.objects.last()
    return render(request, 'about/pages/about.html', {
        "user": user,
        "educations": edus,
        "jobs": jobs,
        "last_job": last_job
    })
