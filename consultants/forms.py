from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Order


# Signup form for user to be flagged as customer or partner
class SignUpForm(UserCreationForm):
    company = forms.CharField(
        label='Company Name', max_length=50, min_length=2)
    vat_no = forms.CharField(max_length=50, label='Enter your VAT')
    CHOICES = ((0, 'Customer'), (1, 'Partner'))
    user_type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',
                  'email',
                  'company',
                  'vat_no',
                  'user_type',)


# Form for user to create new order
class NewOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('title',
                  'role',
                  'period',
                  'startdate',
                  'locality',
                  'duties',
                  'requirements',
                  'wishes',
                  'deadline',
                  )
