from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth.models import User


class SignInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class SignUpForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label = 'confirm_password')
    
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.helper.layout = (
            'username',
            'password', 
            'confirm_password',
            Submit('submit', 'Submit'),
        )
