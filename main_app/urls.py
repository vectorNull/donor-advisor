from django.urls import path

from . import views

urlpatterns = [
    # GENERAL
    path('', views.home_page, name='home'),
    path('contact/', views.contact_page, name='contact'),

    # ORGANIZATIONS
    path('organizations/', views.OrganizationResultsView.as_view(), name='org_results'),
    path('organizations/create', views.organization_create, name='org_create'),
    path('organizations/<int:pk>/', views.OrganizationDetailView.as_view(), name='org_details'),
    path('organizations/<int:pk>/settings/', views.OrganizationUpdateView.as_view(), name='org_update'),
    path('organizations/<int:pk>/delete/', views.organization_delete, name='org_delete'),

    #REVIEWS
    path('organizations/<int:pk>/reviews/create/', views.org_review_create, name='org_review_create'),
    path('organizations/<int:pk>/reviews/<int:review_id>/delete/', views.org_review_delete, name='org_review_delete'),

    #DONATIONS
    path('organizations/<int:pk>/donate/', views.org_donate_create, name='org_donate_create'),

    #GALLERY
    path('organizations/<int:pk>/gallery/create/', views.org_gallery_create, name='org_gallery_create'),
    path('organizations/<int:pk>/gallery/<int:photo_id>/delete/', views.org_gallery_delete, name='org_gallery_delete'),
]