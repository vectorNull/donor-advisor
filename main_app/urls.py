from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    # home ''
    # search from home -> orgs 'organizations/'
    # click from orgs -> orgs id 'organizations/<int:org_id>/'
]