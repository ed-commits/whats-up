from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
#    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
#    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
#    url(r'^register/$', views.register, name='register'),
    url('profile', views.profile, name='profile'),
    url('everyone', views.everyone, name='everyone'),
]
