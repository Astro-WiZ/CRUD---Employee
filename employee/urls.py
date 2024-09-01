from django.urls import path
from employee.views import *


urlpatterns = [
   
    path('employee-id/<int:id>/', idCard, name = "card" ),
    path('add-employee/', addEmployee, name = "add_employee" ),
    path('list-of-employees/', table, name = "list_of_employees" ),
    path('delete-employee/<id>/', delete, name = "delete_employee"),
    path('update-employee/<id>/', update, name = "update_employee"),
    path('',home, name="home")
    
]
