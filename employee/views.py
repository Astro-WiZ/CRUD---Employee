from django.shortcuts import render, redirect,get_object_or_404
from .models import *

# Create your views here.

# Function for creating a new employee
def addEmployee(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        eID  = data.get('eID')
        designation = data.get('designation')
        address = data.get('address')
        picture = request.FILES.get('picture')
        salary = data.get('salary')
        phone = data.get('phone')
        

        new_employee = Employee.objects.create(
            name = name,
            eID = eID,
            designation = designation,
            address = address,
            picture = picture,
            salary = salary,
            phone = phone,
            
        )
        # return redirect('/employee-id/')
        return redirect('card', id = new_employee.id)


    return render(request,"employee.html")


# Function that returns employee ID Card
def idCard(request, id):
    queryset = Employee.objects.get(id = id)
    # queryset = get_object_or_404(Employee, id=id)
    context = {'employee' : queryset}
    
    return render(request, "details.html",context)

# Function to pass employee details in table
def table(request):
    queryset = Employee.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    
    context = {'table': queryset}
    return render(request,'table.html',context)

# delete the employee from table
def delete(request, id):
    queryset = Employee.objects.get(id = id)
    queryset.delete()
    return redirect("/list-of-employees/")


# Update the employee details
def update(request, id):
    queryset = Employee.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        
        name = data.get('name')
        eID = data.get('eID')
        designation = data.get('designation')
        address = data.get('address')
        salary = data.get('salary')
        picture = request.FILES.get('picture')
        phone = data.get('phone')
        
        queryset.name = name
        queryset.eID = eID
        queryset.designation = designation
        queryset.address = address
        queryset.salary = salary
        queryset.phone = phone
        
        if picture:
            queryset.picture = picture
            
        queryset.save()
        return redirect("/list-of-employees/")
        
    context = {'employee': queryset}
    return render(request, "update.html", context)


def home(request):
    return render(request,'index.html')