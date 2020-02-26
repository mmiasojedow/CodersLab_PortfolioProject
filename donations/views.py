from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from donations.models import Donation, Institution


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

        return render(request, 'donations/base.html',
                      {'sacks': sacks_counter, 'institutions': supported_institutions_counter,
                       'foundations': foundations, 'organizations': organizations,
                       'local_collections': local_collections})


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'donations/form.html')
