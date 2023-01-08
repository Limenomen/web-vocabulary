from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import TemplateView


class Login(LoginView):
    template_name = 'core/login.html'

    def get_success_url(self):
        return reverse('core:index')


class Logout(LogoutView):
    def get_success_url(self):
        return reverse('core:index')


class IndexView(TemplateView):
    template_name = 'core/index.html'
