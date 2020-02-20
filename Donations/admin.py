from django.contrib import admin

from Donations.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
