from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, PasswordResetForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from .models import Customer, Invoice

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

class RegistrationForm(UserCreationForm):
  password1 = forms.CharField(
      label=_("Password"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
  )
  password2 = forms.CharField(
      label=_("Password Confirmation"),
      widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype password'}),
  )
  class Meta:
    model = User
    fields = ('username', 'email', )
    labels = {
        "username": "Username",
        "email": "Email",
        }
    widgets = {
      'username': forms.TextInput(attrs={
          'class': 'form-control',
          'placeholder': 'Username'
      }),
      'email': forms.EmailInput(attrs={
          'class': 'form-control',
          'placeholder': 'Email'
      })
    }

# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Username'
#     }))
#     password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Password'
#     }))

####
class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}))

class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}))

#####
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# class UserPasswordResetForm(PasswordResetForm):
#   email = forms.EmailField(widget=forms.EmailInput(attrs={
#     'class': 'form-control',
#     'placeholder': 'Email'
#   }))

# class UserSetPasswordForm(SetPasswordForm):
#     new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'New Password'
#     }), label="New Password")
#     new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Confirm New Password'
#     }), label="Confirm New Password")
    

# class UserPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Old Password'
#     }), label='Old Password')
#     new_password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'New Password'
#     }), label="New Password")
#     new_password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Confirm New Password'
#     }), label="Confirm New Password")

class InvoiceForm(forms.ModelForm):
   class Meta:
      model= Invoice
      fields = '__all__'
   
