from django.urls import path, include
from boss import views 

urlpatterns = [
    path('orders/<int:shop>', views.order_list, name='order_list'),
    path('timeinput/', views.time_input, name='timeinput'),
]