from django.urls import path

from GalaxyOffset.views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('about/', aboutUs, name="about"),
    path('feedback/', feedback, name="feedback"),
    path('contact/', contact, name="contact"),
    path('order/', order, name="order"),
    path('view-profile/', view_profile, name="view-profile"),
    path('edit-profile/', editUser, name="edit-profile"),
    path('change-password/', change_password, name='change-password'),
]
