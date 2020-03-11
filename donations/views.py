from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from donations.forms import DonationForm
from donations.models import Category, Donation, Institution


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
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        form = DonationForm()
        return render(request, 'donations/form.html',
                      {'categories': categories, 'institutions': institutions, 'form': form})

    def post(self, request):
        form = DonationForm(request.POST)
        categories = request.POST['categories']
        institution = request.POST['institution']
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            phone_number = form.cleaned_data['phone_number']
            pick_up_date = form.cleaned_data['pick_up_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            pick_up_comment = form.cleaned_data['pick_up_comment']
            user = request.user.id
            donation = Donation.objects.create(quantity=quantity, institution_id=institution, address=address,
                                               city=city, zip_code=zip_code, phone_number=phone_number,
                                               pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                               pick_up_comment=pick_up_comment, user_id=user)
            donation.categories.add(categories)
            return render(request, 'donations/form-confirmation.html')
        else:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            return render(request, 'donations/form.html',
                          {'categories': categories, 'institutions': institutions, 'form': form})
