from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView
from .models import Order, User
from .forms import SignUpForm, NewOrderForm


class OrderList(generic.ListView):
    model = Order
    queryset = Order.objects.filter(status=0).order_by('created_date')
    template_name = 'orderlist.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class NewOrder(TemplateView):
    template_name = 'new_order.html'

    def get(self, request):
        form = NewOrderForm()
        # responsible = User.objects.get(username=username)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewOrderForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.responsible = request.user
            new_form.save()
            return redirect('/user_orderlist/')
        else:
            return render(request, self.template_name, {'form': form})
