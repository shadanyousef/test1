from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if phone_no and len(phone_no) != 10:
            raise forms.ValidationError("Phone number must have exactly 10 digits.")
        return phone_no