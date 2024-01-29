from django.urls import path
from . import views
urlpatterns=[
path('',views.index,name='index'),
path('events',views.events,name='events'),
path('packages',views.packages,name='packages'),
path('supplies',views.supplies,name='supplies'),
path('menu',views.menu,name='menu'),
path('aboutus',views.aboutus,name='aboutus'),
path('contactus',views.contactus,name='contactus'),
# path('cart',views.cart,name='cart'),


]