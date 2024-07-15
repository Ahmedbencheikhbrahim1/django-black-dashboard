from django.contrib import admin
from django.urls import path
from admin_black import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import login, signup, logout, UserPasswordResetView, UserPasswordResetConfirmView, UserPasswordChangeView

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
     path('factures/', views.factures, name='factures'),
     path('HR/', views.HR, name='HR'),
     path('notifications/', views.notifications, name='notifications'),
     path('user-profile/', views.user_profile, name='user_profile'),
     path('formations/', views.formations, name='formations'),
     path('indexx', views.index, name='index'),

     path('accounts/auth-signup/', views.auth_signup, name = 'auth_signup'),
     path('accounts/auth-signin/', views.AuthSignin, name='auth_signin'),
     path('accounts/forgot-password/', views.UserPasswordResetView.as_view(), name='forgot_password'),

     path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
     path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/logout/', views.user_logout_view, name='logout'),
    path('all_invoices/', views.all_invoices, name='invoices'),
    path('logout/', views.logout, name='logout'),
    # path('signin/', views.signin, name='auth_signup'),
    path('sign/', views.sign, name='auth_sign'),
    path('display_dropdown/', views.display_dropdown, name='display_dropdown'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),


]