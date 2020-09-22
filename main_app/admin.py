from django.contrib import admin
from .models import Organization, Reviews, BoardMembers

# Register your models here.
admin.site.register(Organization)
admin.site.register(Reviews)
admin.site.register(BoardMembers)