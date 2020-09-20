from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import CustomUser
from .forms import LoginForm, RegisterForm

# Create your views here.
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('account_login')

@login_required
def account_profile(request):
    print(request.user.profile_url)
    return render(request, 'accounts/profile.html', {'user': request.user})
