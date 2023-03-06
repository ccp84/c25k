from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("run/list", views.RunList.as_view(), name='run_list'),
    path("run/create", views.RunCreate.as_view(), name='run_create'),
    path("run/update/<pk>", views.RunUpdate.as_view(), name='run_update'),
    path("run/delete/<pk>", views.RunDelete.as_view(), name='run_delete'),
    path("run/run_join/<pk>", views.run_join, name='run_join'),
]
