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
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput
    )
    
    email = forms.CharField(required=True)
    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password1",
            "password2",
        ]

    def clean_email(self):
        """
        If email is already registered,
        enter another email
        """
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(
                u"Email address already exists!"
            )
        return email

    def clean_password2(self):
        """
        if not password or password2 raise error and
        if passwords don't match then raise error
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 or not password2:
            raise ValidationError("Please confirm your password.")

        if password1 != password2:
            raise ValidationError("Passwords do not match!")
        return password2
