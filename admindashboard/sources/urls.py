import imp
from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path ('', views.index, name="sources")
]