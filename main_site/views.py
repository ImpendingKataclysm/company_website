from django.shortcuts import render

from .models import Employee


def home(request):
    return render(request, "index.html")


def team(request):
    employees = Employee.objects.all().values()
    context = {'employees': employees}
    return render(request, "team.html", context=context)
