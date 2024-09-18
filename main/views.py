from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def contact(request):
    if request.method == 'POST':
        name = request.POST.get ['name']
        email = request.POST.get ['email']
        message = request.POST.get ['message']


        send_mail(
            f"Message from {name}",
            message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECEIVER],
            fail_silently=False,
        )

        return render(request, 'contact.html', {'success':True})
    return render(request, 'contact.html')

from django.shortcuts import render

def homepage(request):
    return render(request, 'landing_page.html')  # Ensure this matches your template file
def features(request):
    return render(request, 'features.html')
from django.shortcuts import render

def pricing(request):
    return render(request, 'pricing.html')
def about_us(request):
    return render(request, 'about_us.html')


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect('homepage')  # Redirect to a home page or dashboard
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def check_trial_status(request):
    if request.user.is_authenticated:
        user = request.user
        if user.trial_active and user.is_trial_expired():
            # Deactivate the trial
            user.trial_active = False
            user.save()

            return redirect('payment_page')

@login_required  
def protected_view(request):

    trial_check = check_trial_status(request)
    if trial_check:
        return trial_check  

    context = {
        'some_data': 'This is premium content only available for active trial users or subscribers.'
    }

    return render(request, 'protected_content.html', context)

