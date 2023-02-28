from . import views
from django.urls import path

urlpatterns = [
    path("", views.RunList.as_view(), name='home'),
]
