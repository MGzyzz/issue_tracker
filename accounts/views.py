from django.shortcuts import render, redirect
from django.contrib.auth import views, login
from django.urls import reverse_lazy

from accounts.forms import LoginForm, RegisterForm
from django.views.generic import CreateView
from accounts.models import User
# Create your views here.


class AuthSuccessUrlMixin:
    def get_success_url(self):
        return self.request.GET.get(
            'next',
            self.request.POST.get(
                'next',
                reverse_lazy('home')
            )
        )

class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm

class LogoutView(views.LogoutView):
    def get_next_page(self):
        return self.request.META.get('HTTP_REFERER')

class RegisterView(AuthSuccessUrlMixin, CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())