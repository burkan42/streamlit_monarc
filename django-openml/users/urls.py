#from django.conf.urls import url, include
from django.urls import include, path
                                      
from users.views import dashboard, result

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("result", result, name="result"),
]