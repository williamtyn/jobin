from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('overview', views.OrderList.as_view(), name='overview'),
]