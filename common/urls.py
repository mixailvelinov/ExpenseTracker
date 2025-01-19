from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/create', views.WishCreate.as_view(), name='wishlist-create'),
    path('wishlist/<int:id>/edit/', views.WishEdit.as_view(), name='wishlist-edit'),
    path('wishlist/<int:id>/delete/', views.WishDelete.as_view(), name='wishlist-delete'),
    path('wishlist/buy/<int:id>/', views.wish_buy, name='wishlist-buy'),
    path('wishlist/bought/', views.BoughtItemsListView.as_view(), name='bought-items')

]