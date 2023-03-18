from django.shortcuts import render
import re
from django.http import JsonResponse
from email_validator import validate_email, EmailNotValidError
from .constants import EMAIL_ALREADY_EXIST, PASSWORD_INVALID, SUCCESS, YOU_ARE_NOT_REGISTERED
from .library import isEmpty
from .models import Booking, Users
from passlib.hash import sha256_crypt

# Create your views here.
def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def main(request):
    return render(request, 'main.html')

def booking_confirmation(request):
    if request.method != 'POST':
        return
    placename = request.POST.get("placename")
    num_of_visitors = request.POST.get("num_of_visitors")
    timeSlot = request.POST.get("timeSlot")

    if isEmpty(placename):
        new_data={'data': {}, 'message': 'Please enter Placename', 'status': 0}
        return JsonResponse(new_data)

    if isEmpty(num_of_visitors):
        new_data={'data': {}, 'message': 'Please enter number of visitors', 'status': 0}
        return JsonResponse(new_data)

    if isEmpty(timeSlot):
        new_data={'data': {}, 'message': 'Please enter the timeslot', 'status': 0}
        return JsonResponse(new_data)

    if timeSlot == "05":
        timeSlotValue = "05PM - 07PM"
    elif timeSlot == "12":
        timeSlotValue = "12PM - 01PM"
    else:
        timeSlotValue = "10AM - 11AM"

    try:
        # print("User entered data->", placename, num_of_visitors, timeSlotValue)
        data = Booking(placename=placename, number_of_visitors=num_of_visitors, time_slot=timeSlotValue)
        data.save()
        new_data = {'data': {}, 'message': "Thank you!", 'status': 1}
        return JsonResponse(new_data)
    except Exception as e:
        print(e)

def contact_us(request):
    if request.method != 'POST':
        return
    e_name = request.POST.get("e_name")
    e_mail = request.POST.get("e_mail")
    e_name = request.POST.get("e_name")
    e_subject = request.POST.get("e_subject")
    e_textarea = request.POST.get("e_textarea")
    new_data = {'data': {}, 'message': "Thank you for contacting us! \nWe will revert back to you shortly!", 'status': 1}
    return JsonResponse(new_data)

def login_validation(request):
    if request.method != 'POST':
        return
    email = request.POST.get("email")
    password = request.POST.get("password")

    if isEmpty(email):
        new_data={'data': {}, 'message': 'Please enter email address', 'status': 0}
        return JsonResponse(new_data)

    if isEmpty(password):
        new_data={'data': {}, 'message': 'Please enter your password', 'status': 0}
        return JsonResponse(new_data)

    try:
        xemail = validate_email(email).email # email is validated                    
        if data := Users.objects.filter(uemail=xemail):
            for row in data:
                name = row.name
                userpassword = row.upass

            if (sha256_crypt.verify(password, userpassword)):
                new_data = verifyUser(name, request)
            else:
                new_data = {'data': {}, 'message': PASSWORD_INVALID, 'status': 0}
        else:
            new_data = {'data': {}, 'message': YOU_ARE_NOT_REGISTERED, 'status': 0}
        return JsonResponse(new_data)

    except EmailNotValidError as e:
        print(e)
        print(e)


# TODO Rename this here and in `login_validation`
def verifyUser(name, request):
    request.session['username'] = name
    request.session['userlogin'] = True
    return {
        'data': {'message': 'Logged in successfully'},
        'message': SUCCESS,
        'status': 1,
    }

def signup_validation(request):
    if request.method != 'POST':
        return
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirm_password = request.POST.get("conf_password")

    if isEmpty(name):
        new_data={'data': {}, 'message': 'Please enter name', 'status': 0}
        return JsonResponse(new_data)

    if isEmpty(email):
        new_data={'data': {}, 'message': 'Please enter email address', 'status': 0}
        return JsonResponse(new_data)

    if isEmpty(password):
        new_data={'data': {}, 'message': 'Please enter your password', 'status': 0}
        return JsonResponse(new_data)

    if isEmpty(confirm_password):
        new_data={'data': {}, 'message': 'Please confirm password', 'status': 0}
        return JsonResponse(new_data)

    try:
        email = validate_email(email).email # email is validated

        # CONFIRM IF THE EMAIL IS ALREADY IN THE DATABASE OR NOT
        data = Users.objects.filter(uemail=email)
        if data:
            new_data = {'data': {}, 'message': EMAIL_ALREADY_EXIST, 'status': 0}
        else:
            encrypted_password = sha256_crypt.encrypt(password)
            data = Users(name=name, uemail=email, upass=encrypted_password)
            data.save()
            new_data = {'data': {'message': 'Data has been saved successfully'}, 'message': SUCCESS, 'status': 1}
        return JsonResponse(new_data)

    except EmailNotValidError as e:
        print(e)
        print(e)