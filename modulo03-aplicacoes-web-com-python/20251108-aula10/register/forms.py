from django import forms

class PreRegisterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "id": "email",
            "class": "form-control",
            "placeholder": "E-mail"
        })
    )