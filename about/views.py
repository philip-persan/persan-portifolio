from django.shortcuts import render
from education.models import Education


def about_view(request):
    edus = Education.objects.all()
    return render(request, 'about/pages/about.html', {
        "educations": edus,
    })
