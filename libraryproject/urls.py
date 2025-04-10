"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render
from django.urls import path, include
import apps.bookmodule.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")), 
    path('users/', include("apps.usermodule.urls")),
    path('books/html5/links/', lambda request: render(request, 'books/html5/links/links.html'), name='html5-links'),
    path('books/html5/text/formatting', lambda request: render(request, 'books/html5/text/formatting/formatting.html'), name='html5-links'),
    path('books/html5/text/listing', lambda request: render(request, 'books/html5/text/listing/listing.html'), name='html5-links'),
    path('books/html5/tables/', lambda request: render(request, 'books/html5/tables/tables.html'), name='html5-links'),
    #path('books/html5/search/', lambda request: render(request, 'books/html5/search/search.html'), name='search'),
    
]
