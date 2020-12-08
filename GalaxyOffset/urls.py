from django.contrib.auth import views as auth_views
from django.urls import path

from GalaxyOffset.views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('about/', aboutUs, name="about"),
    path('feedback/', feedback, name="feedback"),
    path('packages/', packages, name="packages"),
    path('order/', order, name="order"),
    path('product/<int:id>', product, name="product"),
    path('view-profile/', view_profile, name="view-profile"),
    path('edit-profile/', editUser, name="edit-profile"),
    path('change-password/', change_password, name='change-password'),

    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='GalaxyOffset/password_reset.html'),
         name="password_reset"),
    path("password-reset/done/",
         auth_views.PasswordResetDoneView.as_view(template_name='GalaxyOffset/password_reset_done.html'),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name='GalaxyOffset/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name='GalaxyOffset/password_reset_complete.html'),
         name="password_reset_complete"),
]
