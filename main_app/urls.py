from django.urls import path

from . import views

urlpatterns = [
    path('accounts/signup/', views.signup, name='signup'),
    # home ''
    # search from home -> orgs 'organizations/'
    # click from orgs -> orgs id 'organizations/<int:org_id>/'
]