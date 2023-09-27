# In your app's forms.py file
from django import forms

class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(label='Shipping Address', max_length=255)
    billing_address = forms.CharField(label='Billing Address', max_length=255)
    payment_method = forms.ChoiceField(label='Payment Method', choices=[('credit_card', 'Credit Card'), ('UPI', 'UPI'), ('Debit Card', 'Debit Card')])
