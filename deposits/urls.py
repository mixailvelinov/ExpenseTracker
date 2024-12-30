from django.urls import path
from deposits import views

urlpatterns = [
    path('', views.DepositView.as_view(), name='deposit')
]