

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

def firstone(request):
    return render(request,'coffeapp/first.html')



def view_emp(request):
    
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request, 'coffeapp/view.html',context)


def add_emp(request):
    if request.method  == "POST":
        first_name=request.POST.get('firstName')
        last_name=request.POST.get('lastName')
        salary=int(request.POST.get('salary'))
        bonus=int(request.POST.get('bonus'))
        dept=int(request.POST.get('dept'))
        role=int(request.POST.get('role'))
        new_emp= Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('employee added Succesfully')
      
    elif request.method=='GET':
        return render(request, 'coffeapp/add.html')
    else:
        return HttpResponse('An error has occured')
       


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('EMployee removed succesfully')
        except Employee.DoesNotExist:
            return HttpResponse('please enter a valid emp Id')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'coffeapp/remove.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        role=request.POST.get('role')
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(Q(dept__name__icontains= dept))
        if role:
            emps=emps.filter(Q(role__name__icontains= role))

        context={
                'emps':emps
         }
        
        return render(request,'coffeapp/view.html',context)
    elif request.method=='GET':
            return render(request,'coffeapp/filter.html')
    else:
            return HttpResponse('an exception error occured')




    
