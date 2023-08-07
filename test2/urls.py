"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from mysire.views import * 
from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ContactCreate.as_view(), name='contact_page'),
    path('reg/', reg),
    path('success/', success, name='success_page'), 
    path('ap/', include('api.urls')),
    path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('books/', books),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

]
