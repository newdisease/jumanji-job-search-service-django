from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from accounts.forms import SignupForm


class MySignupView(CreateView):
    """ Registration """
    form_class = SignupForm
    success_url = '/login'
    template_name = 'accounts/register.html'


class MyLoginView(LoginView):
    """Login"""
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
