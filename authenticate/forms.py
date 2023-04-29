from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
'''user creation form ke lie hai ye normal form k liye ise ues nahi karnan h
normal forms mai ham import karte the'''

'''
from django.contrib.auth import forms

class Sign_up(forms.UserCreationForm):
    pass

is tarike se bhi kar sakte the ham pr use nahi karenge abhi ham ise hai ye dono same hi
'''

''' 'from django import forms' aur class ham 
banate the vo aaise tha - 

class Sign_up(forms.Form):
    pass

'''

class Sign_up(UserCreationForm):   
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

