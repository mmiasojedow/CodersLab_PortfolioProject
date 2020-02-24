from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View

from my_user.forms import RegisterForm

User = get_user_model()


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'my_user/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=email, password=password, email=email, first_name=first_name,
                                     last_name=last_name)
            return redirect('login')
        else:
            return render(request, 'my_user/register.html', {'form': form})
