from django.shortcuts import render
from django.views import View
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
        return render(request, 'base.html', {'sacks': sacks_counter, 'institutions': supported_institutions_counter})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
