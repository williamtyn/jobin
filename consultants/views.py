from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Order, User
from .forms import SignUpForm


class OrderList(generic.ListView):
    model = Order
    queryset = Order.objects.filter(status=0).order_by('created_date')
    template_name = 'orderlist.html'


class HomeView(TemplateView):
    template_name = 'index.html'
