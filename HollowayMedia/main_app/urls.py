from django.urls import path
from django.conf.urls import url
from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('main_app/registration/',views.registration, name='registration'),
    path('main_app/login/',views.user_login,name='login'),
]
