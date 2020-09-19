from django.urls import path, include

from .views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView.as_view(), name='account_login'),
    path('signup/', RegisterView.as_view(), name='account_signup'),
]