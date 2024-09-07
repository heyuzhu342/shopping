from django.urls import re_path, path

from login.views import login, logout, register

urlpatterns = [
    re_path(r'^login', login),
    re_path(r'^logout', logout),
    re_path(r'^register', register),
]