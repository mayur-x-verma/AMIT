from django.shortcuts import render, redirect, reverse, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib import messages
from .forms import FeedbackForm, SubscriptionForm, JobApplicationForm
from .models import Feedback, Subscriber, JobVacancy
import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def service_page(request):
    return render(request, 'service.html')

def service1(request):
    return render(request, 'SWD.html')

def service2(request):
    return render(request, 'WD.html')

def service3(request):
    return render(request, 'MAD.html')

def service4(request):
    return render(request, 'OES.html')

def service5(request):
    return render(request, 'CP.html')

def service6(request):
    return render(request, 'OMR.html')

def service7(request):
    return render(request, 'DPS.html')

def service8(request):
    return render(request, 'ERP.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_and_conditions(request):
    return render(request, 'terms_and_conditions.html')

def clients(request):
    return render(request, 'clients.html') 

logger = logging.getLogger(__name__)

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        logger.debug('Received POST request for subscription')
        try:
            data = json.loads(request.body)
            logger.debug(f'Data received: {data}')
            full_name = data.get('full_name')
            email = data.get('email')
            
            if not full_name or not email:
                raise ValueError("Full name and email are required.")
            
            # Check if the subscriber already exists
            if Subscriber.objects.filter(email=email).exists():
                raise ValueError("This email is already subscribed.")
            
            # Save the subscription to the database
            subscriber = Subscriber(full_name=full_name, email=email)
            subscriber.save()
            logger.debug(f'Subscriber saved: {subscriber}')
            
            # Sending email notification to the host
            subject = 'New Subscriber Alert'
            message = f'New subscriber: {full_name} ({email})'
            from_email = settings.EMAIL_HOST_USER  # Ensure this is set in your settings
            recipient_list = [settings.EMAIL_HOST_USER]  # Change this to your admin email
            
            send_mail(subject, message, from_email, recipient_list)
            logger.debug('Email notification sent')
            
            return JsonResponse({'success': True})
        except Exception as e:
            logger.error(f'Error: {e}')
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def career(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect(reverse('career'))  # Redirect to the same page or any other page
    else:
        form = JobApplicationForm()
    
    job_vacancies = JobVacancy.objects.all()
    
    context = {
        'form': form,
        'job_vacancies': job_vacancies,
    }
    
    return render(request, 'career.html', context)




def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save feedback to the database
            Feedback.objects.create(email=email, message=message)
            try:
                # Send an email to the admin
                send_mail(
                    'New Feedback Received',
                    f'Message from {email}: {message}',
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER],  # Replace with the admin's email address
                    fail_silently=False,
                )
                return JsonResponse({'success': True})  # Return a JSON response on success
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                # Handle other exceptions
                print(f"Error sending email: {e}")
                return JsonResponse({'success': False, 'error': str(e)})
    else:
        form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})