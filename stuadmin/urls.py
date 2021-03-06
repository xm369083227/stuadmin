"""stuadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include,url
from app01.views import classes,students,teachers
from app01.views import classes,students,teachers
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^classes/', classes.classes),
    url(r'^get_stu/', students.get_stu),
    url(r'^add_stu/', students.add_stu),
    url(r'^edit_stu/', students.edit_stu),
    url(r'^del_stu/', students.del_stu),
]
