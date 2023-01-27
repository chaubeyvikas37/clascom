from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.EmployeeView, name = 'home_url'),
    path('v2/', views.EmployeeDisplay, name = 'display_url'),
    path('v3/', views.EmployeeUpdate, name = 'update_url'),
    path('v4/', views.EmployeeDelete, name = 'delete_url')

]