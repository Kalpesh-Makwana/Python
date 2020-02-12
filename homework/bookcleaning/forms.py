from django import forms
from .models import User,City,Cleaner
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

phonenumberexpr=RegexValidator(regex='^[0-9]{10}$',message="Enter Valid Mobile Number")

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('contact','first_name','last_name','email','password1','password2')

class LoginForm(forms.Form):
    contact=forms.CharField(max_length=12,validators=[phonenumberexpr],label='Contact Number')
    password=forms.CharField(max_length=20,label='Password',widget=forms.PasswordInput())

class CleanerForm(forms.ModelForm):
    city=forms.ModelChoiceField(label="Select City",queryset=City.objects.all())
    class Meta:
        model=Cleaner
        fields=["city"]