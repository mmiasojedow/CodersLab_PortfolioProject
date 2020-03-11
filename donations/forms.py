from django import forms
from django.forms import ModelForm

from donations.models import Donation, Institution, Category


# class DonationForm(ModelForm):
#     class Meta:
#         model = Donation
#         fields = '__all__'
#         widgets = {
#             'categories': forms.CheckboxSelectMultiple,
#             'institution': forms.RadioSelect,
#             'address': forms.TextInput(attrs={'placeholder': 'np. Marszałkowska 111/15'}),
#             'city': forms.TextInput(attrs={'placeholder': 'np. Warszawa'}),
#             'zip_code': forms.TextInput(attrs={'placeholder': 'w formacie XX-XXX'}),
#             'phone_number': forms.TextInput(attrs={'placeholder': 'np. 123-456-789'}),
#             'pick_up_date': forms.TextInput(attrs={'type': 'date'}),
#             'pick_up_time': forms.TextInput(attrs={'type': 'time'}),
#             'pick_up_comment': forms.Textarea(attrs={'rows': '5'}),
#         }

class DonationForm(forms.Form):
    quantity = forms.IntegerField()
    categories = forms.ModelChoiceField(queryset=Category.objects.all(),
                                        widget=forms.RadioSelect(attrs={}), empty_label=None)
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(), widget=forms.RadioSelect(attrs={}),
                                         empty_label=None)
    address = forms.CharField(max_length=128)
    phone_number = forms.IntegerField()
    city = forms.CharField(max_length=128)
    zip_code = forms.CharField(max_length=6)
    pick_up_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'mm/dd/yyyy'}))
    pick_up_time = forms.TimeField(widget=forms.TimeInput(attrs={'placeholder': '--:--'}))
    pick_up_comment = forms.CharField(widget=forms.Textarea(attrs={'rows': '5'}), required=False)
