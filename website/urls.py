from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),
    path("thanks/", views.application_success, name="application_success"),
]
