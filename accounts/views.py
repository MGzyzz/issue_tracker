from django.shortcuts import render
from django.contrib.auth import views
from accounts.forms import LoginForm
# Create your views here.
class LoginView(views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class LogoutView(views.LogoutView):
    pass