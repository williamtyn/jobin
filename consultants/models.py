from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    """
    Create custom user as customer or partner
    """

    CHOICES = ((0, 'Customer'), (1, 'Partner'))

    user_type = models.IntegerField(choices=CHOICES, default=0)
    company = models.CharField(max_length=100, default='Company')
    vat_no = models.CharField(max_length=50, default='000000-0000')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.username


# Set status of request if it is active or not due to deadline
STATUS = ((0, 'Active'), (1, 'Inactive'))


class Order(models.Model):
    """
    Data that is being stored for every order created
    """
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    startdate = models.DateField()
    locality = models.CharField(max_length=50)
    duties = models.TextField()
    requirements = models.TextField()
    wishes = models.TextField()
    deadline = models.DateField()
    responsible = models.ForeignKey(
        User,
        on_delete=models.CASCADE, related_name='consultant_request')
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title


class Candidate(models.Model):
    """
    Model for partners to present candidates
    """
    first_name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    cv = CloudinaryField('cv')
    offer = CloudinaryField('offer')
    manager = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='presented_candidates')
    presented_date = models.DateField(auto_now_add=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default="")

    class Meta:
        ordering = ['presented_date', 'manager']

    def __str__(self):
        return f'Candidate {self.first_name} presented by {self.manager}'
