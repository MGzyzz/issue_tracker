from django.shortcuts import render, redirect
from django.contrib.auth import views, login
from django.urls import reverse_lazy, reverse

from accounts.forms import LoginForm, RegisterForm
from django.views.generic import CreateView
from accounts.models import User
# Create your views here.


class AuthSuccessUrlMixin:
    def get_success_url(self):

        next_url = self.request.GET.get('next')

        if not next_url:
            next_url = self.request.POST.get('next')

        if not next_url:
            next_url = reverse('home')

        return next_url

class LoginView(AuthSuccessUrlMixin, views.LoginView):
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

