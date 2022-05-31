from django.shortcuts import render


def portifolio_view(request):
    return render(request, 'work/pages/portifolio.html')
