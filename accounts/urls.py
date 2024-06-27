from django.urls import path

from .views import RegistrationPage

urlpatterns = [
    path("signup/", RegistrationPage.as_view(), name="signup_page"),
]
