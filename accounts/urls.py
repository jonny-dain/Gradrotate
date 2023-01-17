from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

from accounts.forms import UserPasswordResetForm, UserPasswordResetPasswordForm

urlpatterns = [
    path('', views.homepage, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html",form_class=UserPasswordResetForm), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name ="accounts/password_reset_done.html", form_class=UserPasswordResetPasswordForm), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_complete.html"), name="password_reset_complete")

]