"""static_media_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# Django also provides a way to navigate around the different pages in a website.
# When a user requests a URL, Django decides which view it will send it to.

from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf.urls import url

from static_media_app import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^home/', include('static_media_app.urls')),
    path('admin/', admin.site.urls),
]
