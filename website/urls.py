#WEBSITE URLS

from django.urls import path
from website import views

app_name='website'

urlpatterns=[
    path('', views.home, name='home'),
    path('about_us',views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('tos', views.tos, name='tos'),
    path('privacy_policy',views.privacy, name='privacy'),
    path('signup',views.signup, name='signup'),
    path('login', views.login, name='login'),
    

]