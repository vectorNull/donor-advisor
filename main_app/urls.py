from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('organizations/', views.OrganizationResultsView.as_view(), name='org_results'),
]