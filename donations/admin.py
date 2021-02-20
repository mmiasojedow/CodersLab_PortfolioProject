from django.contrib import admin

from donations.models import Category, Donation, Institution

admin.site.register(Category)
admin.site.register(Institution)


class DonationAdmin(admin.ModelAdmin):
    list_display = ['user', 'quantity', 'institution']


admin.site.register(Donation, DonationAdmin)
