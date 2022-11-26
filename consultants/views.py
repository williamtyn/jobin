from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView, CreateView, UpdateView, \
                                 DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.forms import SignupForm
from .models import Order, User, Candidate
from .forms import SignUpForm, NewOrderForm, CandidateForm


class HomeView(TemplateView):
    """
    View for the homepage
    """
    template_name = 'index.html'


class CustomSignUpView(SignupForm):
    """
    View for custom signup as a customer or partner
    """
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'

    def save(form):
        user = form.save()


class LogInView(TemplateView):
    """
    View for redireting user based on which user type
    """
    template_name = 'orderlist.html', 'user_orderlist.html'

    def login_success(request):
        user = request.user
        if user.user_type == 1:
            return redirect('overview')
        else:
            return redirect('user_orderlist')


class UserOrderList(LoginRequiredMixin, TemplateView):
    """
    View for listing a user unique orders and related candidates
    """
    template_name = 'user_orderlist.html'

    def get(self, request):
        user = request.user
        user_orders = user.consultant_request.all()

        candidates = Candidate.objects.all()
        context = {
         'user_orders': user_orders,
         'candidates': candidates
         }

        return render(
            request, self.template_name, context)


class NewOrder(LoginRequiredMixin, TemplateView):
    """
    View for creating a new order for customer
    """
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


class EditOrder(LoginRequiredMixin, UpdateView):
    """
    View for customer to edit a order
    """
    model = Order
    fields = ['title', 'role', 'period', 'startdate', 'locality', 'duties',
              'requirements', 'wishes', 'deadline', 'status', ]
    template_name = 'edit_order.html'
    success_url = reverse_lazy('user_orderlist')


class DeleteOrder(LoginRequiredMixin, DeleteView):
    """
    View for user to delete order
    """
    model = Order
    template_name = 'delete_order.html'
    success_url = reverse_lazy('user_orderlist')


class OrderList(generic.ListView):
    """
    View for listing all active orders for partners to see
    """
    model = Order
    queryset = Order.objects.filter(status=0).order_by('created_date')
    template_name = 'orderlist.html'


class NewCandidate(LoginRequiredMixin, CreateView):
    """
    View for Partner to present a candidate on active order
    """
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
