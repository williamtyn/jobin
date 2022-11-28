from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('redirect/', views.LogInView.as_view(), name='redirect/'),
    path('overview', views.OrderList.as_view(), name='overview'),
    path('new/order', views.NewOrder.as_view(), name='new/order'),
    path('edit/<int:pk>/', views.EditOrder.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteOrder.as_view(), name='delete'),
    path('user/overview', views.UserOrderList.as_view(), name='user/overview'),
    path('new/candidate', views.NewCandidate.as_view(), name='new-candidate'),
]
