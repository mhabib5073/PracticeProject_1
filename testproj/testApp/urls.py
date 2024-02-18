from django.urls import path
from testApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('submit/',views.addEmployee,name='submit'),
    path('edit/<int:pk>/',views.editEmp,name='edit'),
    path('delete/<int:pk>/',views.delete_emp,name='delete'),
]