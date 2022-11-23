from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, User
from .forms import SignUpForm, NewOrderForm, CandidateForm


# View for homepage
class HomeView(TemplateView):
    template_name = 'index.html'


# View for signup as customer or partner
class CustomerSignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'

    def save(form):
        user = form.save()


class LogInView(TemplateView):
    template_name = 'orderlist.html', 'user_orderlist.html'

    def login_success(request):
        user = request.user
        if user.user_type == 1:
            return redirect('overview')
        else:
            return redirect('user_orderlist')


# View for listing a user unique orders to template
class UserOrderList(LoginRequiredMixin, TemplateView):
    template_name = 'user_orderlist.html'

    def get(self, request):
        user = request.user
        user_orders = user.consultant_request.all()

        return render(
            request, self.template_name, {'user_orders': user_orders})


# View for creating a new order for customer
class NewOrder(LoginRequiredMixin, TemplateView):
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
            return redirect('/user_orderlist')
        else:
            return render(request, self.template_name, {'form': form})


# View for user to edit a order
class EditOrder(LoginRequiredMixin, UpdateView):
    model = Order
    fields = ['title', 'role', 'period', 'startdate', 'locality', 'duties',
              'requirements', 'wishes', 'deadline', 'status', ]
    template_name = 'edit_order.html'
    success_url = reverse_lazy('user_orderlist')


# View for user to delete order
class DeleteOrder(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = 'delete_order.html'
    success_url = reverse_lazy('user_orderlist')


# View for listing all active orders for partners to see
class OrderList(generic.ListView):
    model = Order
    queryset = Order.objects.filter(status=0).order_by('created_date')
    template_name = 'orderlist.html'


# View for Partner to present a candidate on active order
class NewCandidate(LoginRequiredMixin, CreateView):
    template_name = 'new_candidate.html'

    def get(self, request):
        form = CandidateForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CandidateForm(request.POST, request.FILES)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.manager = request.user
            new_form.save()
            return redirect('overview')
        else:
            return render(request, self.template_name, {'form': form})
