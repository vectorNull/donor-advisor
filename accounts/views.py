from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm

# Create your views here.
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('account_login')