from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order, Candidate


class SignUpForm(UserCreationForm):
    """
    Signup form for user to be flagged as customer or partner
    """
    company = forms.CharField(
        label='Company Name', max_length=50, min_length=2)
    vat_no = forms.CharField(max_length=50, label='Enter your VAT')
    CHOICES = ((0, 'Customer'), (1, 'Partner'))
    user_type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    email = forms.CharField(max_length=75, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',
                  'email',
                  'company',
                  'vat_no',
                  'user_type',
                  'first_name',
                  'phone',)


class NewOrderForm(forms.ModelForm):
    """
    Form for user to create new order
    """
    startdate = forms.DateField(label='Startdate if hired (YYYY-MM-DD)')
    deadline = forms.DateField(label='Candidate Deadline (YYYY-MM-DD)')
    duties = forms.CharField(label='Describe the consultant duties')
    wishes = forms.CharField(label='What else do you wish for?')
    requirements = forms.CharField(
        label='What requirements do you have? Education/Qualification')

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
                  'deadline',)


class CandidateForm(forms.ModelForm):
    """
    Form for presenting candidate as Partner
    """
    class Meta:
        model = Candidate
        fields = ('first_name',
                  'summary',
                  'price',
                  'cv',
                  'offer',
                  'order',)
