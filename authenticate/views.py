from django.shortcuts import render,HttpResponseRedirect
from .forms import Sign_up
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

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

# def contact(request):
#     if request.POST:
#         name = request.POST['volunteer-name']
#         email = request.POST['volunteer-email']
#         print(name, email, )
#         subject = 'Responce of user'
#         message = 'You responce is' + '\n' + name + '\n' + email + '\n' + subject + '\n' + message
#         email_from = 'kanchanvishwakarma199@gmail.com'
#         # recipient_list = [settings.'EMAIL_HOST_USER']
#         send_mail=(subject, message, email_from,)

#     return render(request,"movie/contect.html")