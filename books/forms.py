from django import forms
from django.contrib.auth.models import User
from books.models import Contact


class LoginPageForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Enter Email'}),label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Enter Password'}),label="")

    class Meta:
        model = User
        fields = ["username","password"]

class RegisterPageForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Enter Username'}),label="")
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Enter First name'}),label="")
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Enter Last name'}),label="")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Enter Email'}),label="") 
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Enter Password'}),label="")  
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Re-enter Password'}),label="")


class ContactForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Enter Mobile no.'}),label="")
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Enter Email'}),label="")
    desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control mb-2','placeholder':'Enter Description'}),label="")

    class Meta:
        model = Contact
        fields = ["phone","email","desc"]