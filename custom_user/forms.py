from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from custom_user.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2')


class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password')


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'phone_number')
