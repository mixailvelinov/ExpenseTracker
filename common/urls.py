from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/create', views.WishCreate.as_view(), name='wishlist-create'),
    path('wishlist/edit/<int:id>/', views.WishEdit.as_view(), name='wishlist-edit'),
    path('wishlist/delete/<int:id>/', views.WishDelete.as_view(), name='wishlist-delete')

]