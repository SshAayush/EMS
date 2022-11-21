from django import forms
from .models import UsersList, Staff

class CustomerForm(forms.ModelForm):
    class Meta:
        model = UsersList
        fields = ['fname', 'lname', 'uname', 'email', 'password','profile_url']
        