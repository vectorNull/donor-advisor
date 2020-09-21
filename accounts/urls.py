from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='account_login'),
    path('signup/', views.AccountRegisterView.as_view(), name='account_signup'),
    path('profile/', views.account_profile, name='account_profile'),
    path('profile/settings/', views.account_profile_update, name='account_update'),
    path('profile/settings/save/', views.account_profile_save, name='account_update_save'),
    path('profile/settings/delete/', views.account_profile_delete, name='account_delete'),
    path('logout/', views.account_logout, name='account_logout'),
]