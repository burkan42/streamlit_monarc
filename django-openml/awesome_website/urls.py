# awesome_website/urls.py

#from django.conf.urls import include, url
from django.urls import include, path

from django.contrib import admin

urlpatterns = [
    path("", include("users.urls")),
    path("admin/", admin.site.urls),
]