from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

TYPES = (
    (1, 'Fundacja'),
    (2, 'Organizacja pozarządowa'),
    (3, 'Zbiórka lokalna'),
)


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        if not self.user:
            return f'for {self.institution}, sacks: {self.quantity}'
        else:
            return f'{self.user} for {self.institution}, sacks: {self.quantity}'
