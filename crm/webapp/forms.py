
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from . models import Record

# Register/create a new user
class CreateUserForm (UserCreationForm):
    class Meta: # Add class meta data
        model = User
        fields = ['username', 'password1', 'password2']

# Login an existing user
class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

# Create a new record
class CreateRecordForm (forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 
                  'address', 'city', 'state', 'country']

# Update an existing record
class UpdateRecordForm (forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 
                  'address', 'city', 'state', 'country']

