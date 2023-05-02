from django.shortcuts import render,HttpResponseRedirect
from .forms import Sign_up
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import Contact,portfolio as Portfolio
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
def home(request):
    if request.method=="POST":
        fm=Sign_up(request.POST)
        if fm.is_valid():
            print("he")
            fm.save()
    else:       
        fm=Sign_up()
    return render(request,'auth/index.html',{'fm':fm})


def log_in(request):
#  if not request.user.is_authenticated:
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            un=fm.cleaned_data['username']
            ps=fm.cleaned_data['password']
            user_auth=authenticate(username=un,password=ps)
            if user_auth is not None:
                login(request,user_auth)
                # return render(request,'auth/profile.html')
                return HttpResponseRedirect('/')

    else:
      fm=AuthenticationForm()
    return render(request,'auth/login.html',{'fm':fm})
#  else:
#     return HttpResponseRedirect("/login/")
def log_out(request):
    logout(request)
    return HttpResponseRedirect("/login/")

def profile(request):
       if request.user.is_authenticated:
            return render(request,'auth/profile.html',{'name':request.user})
       else:
           return HttpResponseRedirect("/login/")
        
      
     
def index(request):
    # if request.method=="POST":
    #     fm=Sign_up(request.POST)
    #     if fm.is_valid():
    #         print("he")
    #         fm.save()
    # else:       
    #     fm=Sign_up()
    return render(request,'auth/index.html')

def contact(request):
    # if request.method == "POST":
    if request.POST:
        name = request.POST['pname']
        email = request.POST['pemail']
        subject = request.POST['psubject']
        message = request.POST['pmassage']
        print(name, email,subject )
        subject = 'Responce of user'
        message = 'You responce is' + '\n' +'name'+ name + '\n' +'email'+ email + '\n' + subject + '\n' + message
        # from_email = settings.EMAIL_HOST_USER
        recipient_list = ['kanchanvishwakarma199@gmail.com']
        send_mail(
            subject='Response from user',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        # contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)

    return render(request,"auth/contact.html")

def portfolio(request,id=None):
    print(id)
    context = {}
    
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio' : portfolio
    }
    return render(request,"auth/portfolio.html",context)

def Service(request):
    return render(request,"auth/service.html")

def about(request):
    return render(request,"auth/about.html")

def profile(request):
    return render(request,"auth/profile.html")