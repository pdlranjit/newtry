
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.firstone,name='firstone'),
    path('view_emp/',views.view_emp, name='view_emp'),
    path('add_emp/',views.add_emp,  name='add_emp'),
    path('remove_emp/',views.remove_emp,  name='remove_emp_list'),
    path('remove_emp/<int:emp_id>/',views.remove_emp,  name='remove_emp'),
 path('filter_emp/',views.filter_emp,  name='filter_emp'),
    
    


   
]