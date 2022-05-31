from django.urls import path

from . import views

app_name = 'work'

urlpatterns = [
    path('', views.portifolio_view, name='index')
]
