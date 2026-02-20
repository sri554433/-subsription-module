from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Payment, Subscription

import json


# LOGIN PAGE
def login_page(request):

    if request.method == "POST":

        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:

            login(request, user)

            return redirect("/plans/")

        else:

            return render(request, "login.html", {
                "error": "Invalid Email or Password"
            })

    return render(request, "login.html")



# REGISTER PAGE
def register_page(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # check password match
        if password != confirm_password:

            return render(request, "register.html", {
                "error": "Passwords do not match"
            })

        # check existing user
        if User.objects.filter(username=email).exists():

            return render(request, "register.html", {
                "error": "Email already registered"
            })

        # create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        return redirect("/")

    return render(request, "register.html")



# LOGOUT
def logout_page(request):

    logout(request)

    return redirect("/")



# PLANS PAGE
@login_required(login_url="/")
def plans_page(request):

    return render(request, "plans.html")



# PAYMENT PAGE
@login_required(login_url="/")
def payment_page(request):

    return render(request, "payment.html", {
        "UPI_ID": settings.UPI_ID,
        "QR_IMAGE": settings.QR_IMAGE
    })



# PROCESSING PAGE
@login_required(login_url="/")
def processing_page(request, payment_id):

    return render(request, "processing.html", {
        "payment_id": payment_id
    })



# SUCCESS PAGE
@login_required(login_url="/")
def success_page(request):

    return render(request, "success.html")



# CREATE PAYMENT AND SUBSCRIPTION
@login_required(login_url="/")
def create_payment(request):

    data = json.loads(request.body)

    plan = data.get("plan")
    method = data.get("method")
    transaction_id = data.get("transaction_id", "")

    prices = {

        "monthly": 499,
        "6months": 2499,
        "yearly": 4499,
        "premium": 5999

    }

    price = prices.get(plan, 499)

    # Save subscription
    Subscription.objects.create(

        user=request.user,
        plan_name=plan,
        price=price

    )

    # Save payment
    payment = Payment.objects.create(

        user=request.user,
        plan=plan,
        amount=price,
        method=method,
        transaction_id=transaction_id,
        status="pending"

    )

    return JsonResponse({

        "payment_id": payment.id

    })



# CHECK PAYMENT STATUS
@login_required(login_url="/")
def check_payment(request, payment_id):

    payment = Payment.objects.get(id=payment_id)

    return JsonResponse({

        "status": payment.status

    })
