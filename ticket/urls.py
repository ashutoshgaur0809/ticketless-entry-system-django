from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('login_validation/', views.login_validation, name="login_validation"),
    path('signup/', views.signup, name="signup"),
    path('signup_validation/', views.signup_validation, name="signup_validation"),
    path('main/', views.main, name="main"),
    path('booking_confirmation/', views.booking_confirmation, name="booking_confirmation"),
    path('contact-us/', views.contact_us, name="contact_us"),
]
