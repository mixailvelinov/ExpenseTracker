from django.urls import path
from expenses import views

urlpatterns = [
    path('', views.ExpensesView.as_view(), name='expenses'),
    path('history/', views.ExpensesHistory.as_view(), name='expenses-history')
]