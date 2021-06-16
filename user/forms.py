from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(label = "İstifadəçi adı")
    password = forms.CharField(label = "Şifrə", widget= forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "İstifadəçi adı")
    mail = forms.CharField(label="Elektron poçt")
    password = forms.CharField(max_length=20,label = "Şifrə",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label = "Təkrar şifrə",widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        mail = self.cleaned_data.get("mail")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifrə dəyərləri eyniləşmir!")
        values = {
            "username": username,
            "mail": mail,
            "password": password,
        }
        return values