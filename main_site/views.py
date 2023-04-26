from django.shortcuts import render
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.contrib import messages
from datetime import datetime

from .models import Employee, Email, Applicant
from .forms import SendEmailForm, ApplicationForm
from .functions import handle_validation_error


def home(request):
    return render(request, "index.html")


def team(request):
    employees = Employee.objects.all().values()
    context = {'employees': employees}
    return render(request, "team.html", context=context)


def about(request):
    return render(request, "about.html")


def contact(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)

        if form.is_valid():
            sender_name = form.cleaned_data["sender_name"]
            sender_email = form.cleaned_data["sender_email"]
            message = form.cleaned_data["message"]

            # Store the message in a database
            Email.objects.create(sender_name=sender_name,
                                 sender_email=sender_email,
                                 date_sent=datetime.now(),
                                 message=message)

            # Email sending functionality not implemented at this time
            # No app password configured
            email_subject = f"Message received from {sender_name} ({sender_email})"
            email_message = EmailMessage(subject=email_subject,
                                         body=message,
                                         to=[settings.EMAIL_HOST_USER])
            # email_message.send()

            # Display a success message in the browser
            success_message = f"Thanks for reaching out, {sender_name.title()}!"
            messages.success(request, success_message)
        else:
            handle_validation_error(request)

    return render(request, "contact.html")


def careers(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            # Get the applicant's information
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date_applied = datetime.now()
            date_available = form.cleaned_data["start_date"]
            employment_status = form.cleaned_data["employment_status"]

            # Save the applicant's resume in the 'resume' folder
            f = request.FILES['resume']
            with open(f'main_site/static/resumes/{last_name}_{first_name}_{f.name}', 'wb+') as dest:
                for chunk in f.chunks():
                    dest.write(chunk)

            # Save the applicant in the database
            Applicant.objects.create(first_name=first_name,
                                     last_name=last_name,
                                     email=email,
                                     date_applied=date_applied,
                                     date_available=date_available,
                                     employment_status=employment_status)

            # Display a success message in the browser
            success_message = f"Thanks for your application, {first_name.title()} {last_name.title()}"
            messages.success(request, success_message)
        else:
            handle_validation_error(request)

    return render(request, "careers.html")
