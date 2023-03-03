from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("run/list", views.RunList.as_view(), name='run_list'),
    path("run/create", views.RunCreate.as_view(), name='run_create'),
    path("run/update/<pk>", views.RunUpdate.as_view(), name='run_update')
]
