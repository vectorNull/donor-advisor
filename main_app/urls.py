from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contact_page, name='contact'),
    path('organizations/', views.OrganizationResultsView.as_view(), name='org_results'),
    path('organizations/create', views.organization_create, name='org_create'),
    path('organizations/<int:pk>/', views.OrganizationDetailView.as_view(), name='org_details'),
    path('organizations/<int:pk>/settings/', views.OrganizationUpdateView.as_view(), name='org_update'),
    path('organizations/<int:pk>/delete/', views.organization_delete, name='org_delete'),
]