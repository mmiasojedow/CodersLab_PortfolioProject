from django.shortcuts import render
from django.views import View

from Donations.models import *


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

        foundations = Institution.objects.filter(type=1)
        organizations = Institution.objects.filter(type=2)
        local_collections = Institution.objects.filter(type=3)

        # page = request.GET.get('page')
        # paginator_foundations = Paginator(foundations_list, 1)
        # paginator_organizations = Paginator(organizations_list, 1)
        # paginator_local = Paginator(local_list, 1)
        #
        # foundations = paginator_foundations.get_page(page)
        # organizations = paginator_organizations.get_page(page)
        # local_collections = paginator_local.get_page(page)
        return render(request, 'base.html',
                      {'sacks': sacks_counter, 'institutions': supported_institutions_counter,
                       'foundations': foundations, 'organizations': organizations,
                       'local_collections': local_collections})


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')
