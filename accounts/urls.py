from django.urls import path, include

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('signup/', views.RegisterView.as_view(), name='account_signup'),
    path('profile/', views.account_profile, name='account_profile'),
]