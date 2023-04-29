from django.urls import path
from . import views
urlpatterns=[
    path('',views.profile,name="profile"),
    path('signup/',views.home,name="signup"),
    path('login/',views.log_in,name="login"),
    path('logout/',views.log_out,name="logout"),
    path('index/',views.profile,name="index"),
#     path('contact/',views.profile,name="contact"),
]