from django.urls import path
#from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name='menu'),
    path('menu-item/<int:pk>/', views.menu_item, name='menu-item'),
    path('book/', views.Book.as_view(), name='book'),
    path('bookings/', views.bookings, name='bookings'),
]




#urlpatterns = [
  #  path('', index, name='index'),
  #  path('menu/', MenuView.as_view()),
  #  path('booking/', Bookingview.as_view()),
  #  path('menu-items/', MenuItemListView.as_view()),
  #  path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
   # path('message/', msg),
   # path('api-token-auth/', obtain_auth_token),
   # path('managerview', manager_view),
   ##  path('bookings/<int:pk>', SingleBookingView.as_view(), name='booking-detail'),
#]


