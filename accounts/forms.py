from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(max_lenght=20)
    