"""piglatin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Steps to add a page:
# 1. create a new .py file
# 2. add the file to the urls.py  file like so "from . import <new file name>.py"
# 3. add the page and the method to the urlpatterns list like so "url (/r'^<url sub domain>/', <filename>.<methodname>")

from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about'),
    url(r'^newpage/', views.newpage, name='newpage')

]
