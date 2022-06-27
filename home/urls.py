from django.urls import path
from .views import *

urlpatterns = [
	path('',HomeView.as_view(),name = 'home'),
	path('subcat/<slug>',SubcategoryView.as_view(),name = 'subcat'),
	path('detail/<slug>',DetailView.as_view(),name = 'detail'),
	path('search/',SearchView.as_view(),name = 'search'),
	path('register/',signup,name = 'register'),
	path('login/',login, name = 'login'),
	path('logout/',logout, name = 'logout'),
	path('cart/<slug>',cart,name = 'cart'),
    path('my_cart/',CartView.as_view(),name = 'my_cart'),
    path('delete_cart/<slug>',delete_cart, name = 'delete_cart'),
    path('reduce_cart/<slug>',reduce_cart, name = 'reduce_cart'),
    path('about/',aboutView.as_view(),name='about'),
    path('codes/',codesView.as_view(),name='codes'),
    path('kitchen/',kitchenView.as_view(),name='kitchen'),
    path('personalcare/',personalcareView.as_view(),name='personalcare'),
    path('household/',householdView.as_view(),name='household'),
    path('shipping/',shippingView.as_view(),name='shipping'),
    path('terms/',termsView.as_view(),name='terms'),
    path('faqs/',faqsView.as_view(),name='faqs'),
    path('contact/',contact, name='contact'),
    path('checkout/',checkoutView,name='checkout'),
    path('payment/',paymentView.as_view(),name='payment'),

]

