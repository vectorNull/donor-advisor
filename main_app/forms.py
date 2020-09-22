from django.forms import ModelForm

from .models import Organization

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = [
            'name', 'ein', 'address', 'city', 
            'description','mission_statements','state', 'zip_code',
            'phone','contact_email','website_url', 'category',
            'fiscal_sponsor','guidestar_url',
        ]