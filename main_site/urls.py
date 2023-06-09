from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("team/", views.team, name="team"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("careers/", views.careers, name="careers")
]
