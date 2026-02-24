#pasnevesht urls

from django.urls import path
from blog import views

app_name='blog'

urlpatterns=[
    path('', views.home, name='home'),
    path('full_post-<int:pid>', views.full_post, name='full_post')
]