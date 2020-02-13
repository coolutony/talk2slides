from django.urls import path

from . import views

app_name = 'record'
urlpatterns = [
    path('', views.index, name='index'),
    path('receive', views.receive, name='receive'),
]