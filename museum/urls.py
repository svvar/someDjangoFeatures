from django.urls import path, re_path
from . import views

app_name = 'museum'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^tickets/?$', views.tickets, name='tickets'),
    # re_path(r'^about/?$', views.about, name='about'),
]