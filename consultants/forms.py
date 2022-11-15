from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    company = forms.CharField(
        label='Company Inc', max_length=50, min_length=2)
    vat_no = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'company',
                  'vat_no', )
