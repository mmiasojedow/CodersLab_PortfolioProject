from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.core.paginator import Paginator

from OddamWDobreRece.forms import RegistrationForm, LoginForm
from OddamWDobreRece.models import *


# Create your views here.


class LandingPageView(View):
    def get(self, request):
        sacks_counter = 0
        supported_institutions = []
        donations = Donation.objects.all()
        for donation in donations:
            sacks_counter += donation.quantity
            if donation.institution.name not in supported_institutions:
                supported_institutions.append(donation.institution.name)
        supported_institutions_counter = len(supported_institutions)

        foundations_list = Institution.objects.filter(type=1)
        organizations_list = Institution.objects.filter(type=2)
        local_list = Institution.objects.filter(type=3)

        page = request.GET.get('page')
        paginator_foundations = Paginator(foundations_list, 5)
        paginator_organizations = Paginator(organizations_list, 5)
        paginator_local = Paginator(local_list, 5)

        foundations = paginator_foundations.get_page(page)
        organizations = paginator_organizations.get_page(page)
        local_collections = paginator_local.get_page(page)
        return render(request, 'base.html',
                      {'sacks': sacks_counter, 'institutions': supported_institutions_counter,
                       'foundations': foundations, 'organizations': organizations,
                       'local_collections': local_collections})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                return redirect('register')
        else:
            return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('main')


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

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
            return render(request, 'register.html', {'form': form})
