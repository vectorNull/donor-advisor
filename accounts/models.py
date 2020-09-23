from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    description = models.TextField(max_length=250)
    profile_url = models.CharField(max_length=200, default="https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png")

    def __str__(self):
        return self.email

    def full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'

    def is_partial_complete(self):
        return self.first_name and self.last_name and self.email
    
    def is_complete(self):
        return self.is_partial_complete() and self.description and self.profile_url
