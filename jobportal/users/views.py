from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == User.ROLE_EMPLOYER:
                return redirect('employer_dashboard')
            else:
                return redirect('applicant_dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    def get_success_url(self):
        if self.request.user.role == User.ROLE_EMPLOYER:
            return '/employer/dashboard/'
        else:
            return '/applicant/dashboard/'
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

class LoginView(DjangoLoginView):
    template_name = 'users/login.html'

class LogoutView(DjangoLogoutView):
    template_name = 'users/logged_out.html'  
