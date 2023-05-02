from django.urls import path
from . import views
urlpatterns=[
    path('',views.profile,name="profile"),
    path('signup/',views.home,name="signup"),
    path('login/',views.log_in,name="login"),
    path('logout/',views.log_out,name="logout"),
    path('index/',views.profile,name="index"),
    path('contact/',views.contact,name="contact"),
    path('portfolio/',views.portfolio,name="portfolio"),
    path('service/',views.Service,name="service"),
    path('about/',views.about,name="about"),
    path('profile/',views.profile,name="profile"),
    path('portfolio/',views.portfolio,name="portfolio"),
    # path('portfolio/<int:id>/',views.portfolio,name="portfolio"),
#     path('linkedin/<str:username>/', views.linkedin_profile, name='linkedin_profile'),
]
