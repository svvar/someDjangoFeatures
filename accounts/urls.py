from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/?$',views.SignUp.as_view(),name='signup'),
    re_path(r'^login/?$',views.Login.as_view(),name = 'login'),
    re_path(r'^logout/?$',LogoutView.as_view(),name='logout'),
    re_path(r'^profile/?$',views.profile, name='profile')
]