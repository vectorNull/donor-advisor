from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q

from .models import Organization

# Create your views here.
def home_page(request):
    return render(request, 'main_app/home.html')

class OrganizationResultsView(ListView):
    model = Organization
    template_name = 'main_app/organizations/results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        location = self.request.GET.get('l')
        category = self.request.GET.get('c')
        if not query and not location and not category:
            print(True)
            return Organization.objects.order_by('-name').all()
        if not query:
            query = 'None'
        if not location:
            location = 'None'            
        if not category:
            category = 'None'
        return Organization.objects.filter(
            Q(name__icontains=query) |
            Q(ein__icontains=query) |
            Q(address__icontains=location) |
            Q(city__icontains=location) |
            Q(state__icontains=location) |
            Q(zip_code=location) |
            Q(category__icontains=category)
        )