from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('<int:id>/', views.user_details, name='details'),
    path('<int:id>/edit/', views.UserUpdateView.as_view(), name='edit'),
    path('<int:id>/delete/', views.user_delete_view, name='delete'),
    path('<int:id>/profile/', views.ProfileUpdateView.as_view(), name='profile')

]