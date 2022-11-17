from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewOrderForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.responsible = request.user
            new_form.save()
            # added request.user.order.add(new_form)  
            return redirect('/user_orderlist/')
        else:
            return render(request, self.template_name, {'form': form})


class UserOrderList(LoginRequiredMixin, TemplateView):
    template_name = 'user_orderlist.html'

    def get(self, request):
        user = request.user
        user_orders = user.consultant_request.all()

        return render(
            request, self.template_name, {'user_orders': user_orders})

