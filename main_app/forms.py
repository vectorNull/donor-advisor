from django.forms import ModelForm

from .models import Organization

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        labels = {
            'description': 'About Us',
            'mission_statement': 'Mission Statement'
        }
        fields = [
            'name', 'ein', 'address', 'city', 
            'state', 'zip_code', 'phone','contact_email','website_url', 'category',
            'fiscal_sponsor','guidestar_url', 'logo_url','mission_statement', 'description',
        ]