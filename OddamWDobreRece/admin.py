from django.contrib import admin
from OddamWDobreRece.models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']


class InstitutionAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'type', 'categories']

class DonationAdmin(admin.ModelAdmin):
    fields = ['quantity', 'categories', 'institution', 'address', 'phone_number', 'city', 'zip_code', 'pick_up_date', 'pick_up_time', 'pick_up_comment', 'user']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Donation, DonationAdmin)

