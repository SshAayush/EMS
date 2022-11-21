# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html', {})

from http.client import HTTPResponse
from telnetlib import AUTHENTICATION
from tokenize import generate_tokens
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from EMS import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes#,force_text
#from .tokens import generate_token
from django.core.mail import EmailMessage,send_mail
#from django.contrib.auth.views import PasswordResetView
#from django.utils.encoding import force_text
#from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.decorators import login_required
from .models import UsersList, Staff, Time
from .forms import CustomerForm
from datetime import datetime
# Create your views here.

def home(request):
    return render(request, "authentication/signin.html", {})

@login_required
def dashboard(request):
    return render(request, "authentication/dashboard.html")


@login_required
def staff(request):
    return render(request, "authentication/home.html")

# @login_required
def table(request):
    all_users = UsersList.objects.all
    return render(request, "authentication/table.html", {'all':all_users})

# @login_required
def additional_info(request, pk):
    if request.method == 'GET':
        t = UsersList.objects.get(id=pk)
        fname = t.fname
        lname = t.lname
        email = t.email
        password = t.password
        profile_url = t.profile_url
        starttime = t.starttime
    return render(request, "authentication/additional_info.html", {'f':fname, 'l':lname, 'e':email, 'p':password, 'url':profile_url, 'start':starttime})

# @login_required
# def additional_info(request):
#     all_users = UsersList.objects.filter(UsersList__uid=request.UsersList.uid)
#     return render(request, "authentication/additional_info.html", {'all':all_users})

# @login_required
def homepg(request):
    current_user = request.user
    logged_user = current_user.id
    all_staffs = Staff.objects.all
    return render(request, "authentication/home.html", {'all':all_staffs, 'userinfo':logged_user})


#clock in clock out

def clockin(request, pk):
    if request.method == 'GET':
        t = Staff.objects.get(id=pk)
        t.s_status = True
        t.s_starttime = datetime.now()
        t.save()
        return redirect('staff')
    else:
        return redirect('staff')

def clockout(request, pk):
    if request.method == 'GET':
        t = Staff.objects.get(id=pk)
        t.s_status = False
        t.s_endtime = datetime.now()
        t.save()
        return redirect('staff')
    else:
        return redirect('staff')

# @login_required
def customer_join(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        profile_url = request.POST['profile_url']
        new_customer = UsersList(fname = fname, lname = lname, uname = uname, email = email, password = password, starttime = datetime.now(), profile_url = profile_url)
        new_customer.save()
        messages.success(request, "Staff Account Has Been Created.")
        return redirect('table')
    
    else:
        return render(request, "authentication/add_customer.html", {})
        # return render(request, "authentication/table.html", {})
        # return redirect('customer_join')

# @login_required
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('signup')

        if len(username)>15:
            messages.error(request, "Username length long max.15!")

        if password1 != password2:
            messages.error(request, "Password doesn't Match!")

        # if not username.isalnum():
        #     messages.error(request, "Username must be alphanumeric!")
        #     return redirect('signup')
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.password2 = password2
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Staff Account Has Been Created.")
        
        #Test to add and view staff info
        s_fname = request.POST['fname']
        s_lname = request.POST['lname']
        s_Email = request.POST['email']
        new_staff = Staff(s_fname = s_fname, s_lname = s_lname, s_Email = s_Email, s_starttime = datetime.now(), s_endtime = datetime.now())
        new_staff.save()


        #Welcome Email

        subject = "Welcome to EMS!"
        # message = "Hello " + myuser.first_name + "! ! \n" + "Welcome to Project Stream! \nWe're so happy you're here. We founded Project Stream because we wanted to create a trustworthy and inspiring place for you to find everything you need to stream and live well.\n\n With Best Regards,\n Team Project Stream"
        message = "Hello " + myuser.first_name + "!! \n\n" + "Welcome to Staff Management System! \n\nYour Credentials are: \nUsername: "+ username +"\nPassword: "+ password1 +"\n\nKeep your credentials safe!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        
        return redirect('staff')   

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')

        user = authenticate(username=username, password=password1) #error may come

        if user is not None:
            login(request, user)
            fname = user.first_name
            return redirect('table')
            # return render(request, "authentication/table.html", {'fname': fname})

        else:
            messages.error(request, "Invalid Credentials")
            # return redirect('signup')  --> wrong password hanyo vane signup ma redirect gar xa
        
        # return redirect('signup') ---->test to redirect ti staff page

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    #messages.success(request, "Logged Out Successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_tokens.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
