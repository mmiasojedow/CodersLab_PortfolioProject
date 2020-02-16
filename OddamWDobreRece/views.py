from django.shortcuts import render
from django.views import View
from OddamWDobreRece.models import *
from django.core.paginator import Paginator


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
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
