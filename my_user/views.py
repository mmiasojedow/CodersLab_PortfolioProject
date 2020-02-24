from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import FormView

from my_user.forms import LoginForm, RegistrationForm
from my_user.models import User


# Create your views here.


# class LoginView(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'my_user/login.html', {'form': form})
#
#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('main')
#             else:
#                 return redirect('register')
#         else:
#             return render(request, 'my_user/login.html', {'form': form})

class LogInView(LoginView):
    template_name = 'my_user/login.html'
    authentication_form = LoginForm


class LogOutView(LogoutView):
    next_page = 'main'


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'my_user/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=email, password=password, email=email, first_name=name, last_name=surname)
            return redirect('login')
        else:
            return render(request, 'my_user/register.html', {'form': form})