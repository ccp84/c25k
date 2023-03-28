from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("run/list", views.RunList.as_view(), name='run_list'),
    path("run/create", views.RunCreate.as_view(), name='run_create'),
    path("run/update/<pk>", views.RunUpdate.as_view(), name='run_update'),
    path("run/delete/<pk>", views.RunDelete.as_view(), name='run_delete'),
    path("run/run_join/<pk>", views.run_join, name='run_join'),
    path("profile/create",
         views.ProfileCreate.as_view(), name='profile_create'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("profile/update/<pk>",
         views.ProfileUpdate.as_view(), name='profile_update'),
    path("profile/delete/<pk>",
         views.ProfileDelete.as_view(), name='profile_delete'),
    path("runner/<id>", views.RunnerProfile.as_view(), name='runner_profile'),
    path("user/list", views.UserList.as_view(), name='user_list'),
    path("user/make_leader/<id>", views.make_leader, name='make_leader'),
    path("user/remove_leader/<id>", views.remove_leader, name='remove_leader'),
]
handler404 = 'register.views.page_not_found_custom'
handler500 = 'register.views.page_error_found_custom'
