from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('organizations/', views.OrganizationResultsView.as_view(), name='org_results'),
    path('organizations/create', views.organization_create, name='org_create'),
    path('organizations/<int:pk>/', views.OrganizationDetailView.as_view(), name='org_details'),
]