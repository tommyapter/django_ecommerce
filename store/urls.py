from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('payment/', views.payment, name="payment"),

    path('add_to_cart/<int:product_id>', views.add_to_cart, name="add_to_cart"),
    path('add_one/<int:orderitem_id>', views.add_one, name="add_one"),
    path('remove_one/<int:orderitem_id>', views.remove_one, name="remove_one"),
	path('process_order/', views.process_order, name="process_order"),
]
