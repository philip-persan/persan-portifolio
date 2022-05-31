from django.urls import path

from . import views

app_name = "skills"

urlpatterns = [
    path('', views.skills_view, name='index')
]
