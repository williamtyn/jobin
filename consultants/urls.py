from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('overview', views.OrderList.as_view(), name='overview'),
    path('new_order', views.NewOrder.as_view(), name='new'),
    path('edit/<int:pk>/', views.EditOrder.as_view(), name='edit'),
    path('user_orderlist', views.UserOrderList.as_view(), name='user_orderlist'),
]