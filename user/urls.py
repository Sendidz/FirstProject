from user import views
from django.urls import path, include


urlpatterns=[
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name = 'register')
]