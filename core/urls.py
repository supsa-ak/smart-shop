from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    Login,
    SignUp,
    Logout,
    # PaymentView,
    # AddCouponView,
    # RequestRefundView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('login/', Login, name='login'),
    path('signup/', SignUp, name='signup'),
    path('logout/', Logout, name='logout'),

    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # path('request-refund/', RequestRefundView.as_view(), name='request-refund')
] 

from django.contrib import admin
# from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
# from django.contrib.sites.models import Site

# admin.site.unregister(Site)
# admin.site.unregister(SocialToken)
# admin.site.unregister(SocialAccount)
# admin.site.unregister(SocialApp)