from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Channel_Integration_Form, Carrier_Integration, User_signup_form, User_login_form, Pickup_form_1, Order_Form, Track_Order
from .forms import OTP_Verification
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.forms.models import model_to_dict
# Create your views here.

from .models import CustomUser,Account, Recharge_Transaction, Order
from courierproject import settings

def home(request):
    context = {'user':request.user.is_authenticated}
    return render(request,"project/home.html",context)

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        form = User_login_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                form = login(request, user)
                return redirect('home')
    user_form = User_login_form()
    context = {'form':user_form,'error':user_form.errors,'user':request.user.is_authenticated}
    return render(request,"project/login_page.html",context)

@csrf_exempt
def user_signup(request):
    user_form = User_signup_form(request.POST or None)
    if request.method == "POST":
        if user_form.is_valid():
            email = user_form.save()
            user = CustomUser.objects.filter(email=email)[0]
            account = Account(user=user,account_balance=0)
            account.save()
            return redirect("/otp_verification")
    context = {'form':user_form,'error':user_form.errors,'user':request.user.is_authenticated}
    return render(request,"project/signup_page.html",context)

@csrf_exempt
def otp_verification(request):
    otp='1234'
    if request.method == "POST":
        form = OTP_Verification(request.POST)
        if form.is_valid():
            if form.cleaned_data['mobile_otp'] == otp and form.cleaned_data['email_otp'] == otp:
                return redirect("/")
    form = OTP_Verification()
    context={'form':form,'error':form.errors}
    return render(request,"project/otp-verification.html",context)

def user_logout(request):
    if request.user.is_authenticated:
        print(request.user)
    logout(request)
    if not request.user.is_authenticated:
        print(request.user)
    return redirect('/')

def about_us(request):
    return render(request,"project/about_us.html")

def contact_us(request):                                                                                                                                                      
    return render(request,"project/contact_us.html")

@csrf_exempt
def track_order(request):
    form = Track_Order()
    context = {'form':form,'user':request.user.is_authenticated}
    return render(request,"project/track_order.html",context)

@csrf_exempt
def channel_integration(request):
    if request.method == "POST":
        form = Channel_Integration_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = Channel_Integration_Form()
    context = {'form':form,'user':request.user.is_authenticated}
    return render(request,"project/channel_integration.html",context)

@csrf_exempt
def carrier_integration(request):
    if request.method == "POST":
        form = Carrier_Integration(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = Carrier_Integration()
    context = {'form':form,'user':request.user.is_authenticated}
    return render(request,"project/carrier_integration.html",context)

def page_not_found(request,exception):
    return render(request,"project/404.html",status=404)

@csrf_exempt
def order1(request):
    if request.method == "POST":
        return redirect('order2')
    form = Pickup_form_1()
    context = {'form':form,'user':request.user.is_authenticated}
    return render(request,"project/pickup1.html",context)

@csrf_exempt
def order2(request):
    if request.method == "POST":
        return redirect('order3')
    return render(request,"project/pickup2.html")

@csrf_exempt
def order3(request):
    if request.method == "POST":
        form = Order_Form(request.POST,request.FILES)
        if form.is_valid():
                id = form.save()
                print("order saved")
                order_id = id.id
                print("got order id")
                order_details = Order.objects.filter(id = order_id)[0]
                order_details = Order_Form(data=model_to_dict(Order.objects.get(pk=order_id)))
                print("got order details")
                context = {'order_details': order_details}
                print("created context")
                return render(request, "project/order-confirm.html", context)
    form = Order_Form()
    context = {'form':form,'user':request.user.is_authenticated}
    return render(request,"project/pickup3.html",context)


def profile_page(request):
    first_name, last_name, email, mobile_no  = 'Not Provided', 'Not Provided', 'Not Provided', 'Not Provided'
    context = {'first_name':first_name,'last_name':last_name,'mobile_no':mobile_no,'email':email,'mobile_no':mobile_no , 'balance': 0}
    try:
        if request.user.is_authenticated:
            first_name = request.user.first_name
            last_name = request.user.last_name
            email = request.user.email
            mobile_no = request.user.mobile_no
            user = CustomUser.objects.filter(email=request.user)[0]
            balance = Account.objects.filter(user=user)[0].account_balance
            print(balance)
            context['balance'] = balance
    except:
        pass
    return render(request,"project/profile_page.html",context)
