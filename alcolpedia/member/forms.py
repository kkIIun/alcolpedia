from django import forms
from phonenumber_field.modelfields import PhoneNumberField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
class UserAccounts(forms.Form):
    name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Surname', max_length=100)
    phone_number = PhoneNumberField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    verify_password = forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'POST'
        self.helper.layout = (
            'name', 
            'last_name',
            'phone_number',
            'email', 
            'password', 
            'verify_password',
            Submit('submit', 'Submit'),
        )