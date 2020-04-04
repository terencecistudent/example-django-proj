from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    """
    Form to be used for user login
    """
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    """
    Form used for new user registration
    """
    # format for password creation
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password",
            "password2",
        ]

    def check_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u"Please enter a unique email address.")
        return email

    def check_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        # if not password or password2 raise error
        if not password or not password2:
            raise forms.ValidationError("Please confirm you password.")

        # if passwords don't match then raise error
        if password != password2:
            raise forms.ValidationError("Passwords do not match!")
        return password2
