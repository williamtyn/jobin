from django.db import models
from django.contrib.auth.models import AbstractUser


# Create custom user as customer or partner
class User(AbstractUser):

    CHOICES = ((0, 'Customer'), (1, 'Partner'))

    user_type = models.IntegerField(choices=CHOICES, default=0)
    company = models.CharField(max_length=100, default='Company')
    vat_no = models.CharField(max_length=50, default='000000-0000')

    def __str__(self):
        return self.username


# Set status of request if it is active or not due to deadline
STATUS = ((0, 'Active'), (1, 'Inactive'))


# Content in every request
class Order(models.Model):
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    startdate = models.DateTimeField()
    locality = models.CharField(max_length=50)
    duties = models.TextField()
    requirements = models.TextField()
    wishes = models.TextField()
    deadline = models.DateTimeField()
    responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='consultant_request')
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title
