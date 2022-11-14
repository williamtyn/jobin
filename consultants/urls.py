from . import views
from django.urls import path


urlpatterns = [
    path('', views.OrderList.as_view(), name='home')
]