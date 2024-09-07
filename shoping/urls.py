"""shoping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

import goodsIssue.urls
import login.urls
import trade.urls
from tiaozao import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    re_path(r'^search', views.search),
    re_path(r'^login/', include(('login.urls', "login"), namespace='login')),
    re_path(r'^goodsIssue/', include(('goodsIssue.urls', 'goodsIssue'), namespace='goodsIssue')),
    re_path(r'^trade/', include(('trade.urls', 'trade'), namespace='trade')),

]
