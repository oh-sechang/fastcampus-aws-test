from django.urls import path, include
from delivery import views 

urlpatterns = [
    path('orders/', views.order_list, name='order_list')
    # path('orders/<int:shop>', views.order_list, name='order_list'),
    # path('timeinput/', views.time_input, name='timeinput'),
]