from django.shortcuts import render
from datetime import datetime
from django.core.mail.message import EmailMessage
from django.conf import settings

from .models import Employee, Email
from .forms import SendEmailForm


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

            # Email sending functionality not implemented at this time
            # No app password configured
            email_subject = f"Message received from {sender_name} ({sender_email})"
            email_message = EmailMessage(subject=email_subject,
                                         body=message,
                                         to=[settings.EMAIL_HOST_USER])
            # email_message.send()

    return render(request, "contact.html")
