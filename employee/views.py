from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# Function for creating a new employee
@login_required(login_url="/login")
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
@login_required(login_url="/login")
def idCard(request, id):
    queryset = Employee.objects.get(id = id)
    # queryset = get_object_or_404(Employee, id=id)
    context = {'employee' : queryset}
    
    return render(request, "details.html",context)

# Function to pass employee details in table
@login_required(login_url="/login")
def table(request):
    queryset = Employee.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    
    context = {'table': queryset}
    return render(request,'table.html',context)

# delete the employee from table
@login_required(login_url="/login")
def delete(request, id):
    queryset = Employee.objects.get(id = id)
    queryset.delete()
    return redirect("/list-of-employees/")


# Update the employee details
@login_required(login_url="/login")
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


def login_page(request):
    
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"User doesn't exist")
            return redirect("/login/")
        
        user = authenticate(username=username,password=password)
        
        if user is None:
            messages.error(request,"Invalid Password.")
            return redirect("/login/")
        
        else:
            login(request,user)
            return redirect("/list-of-employees/")
        
        
    if request.user.is_authenticated:
        messages.info(request,"User Logged Out.")
        logout(request)     
    return render(request, "login.html")

def logout_page(request):
    logout(request)
    messages.info(request,'logout successful.')
    return redirect("/login/")
    

def register(request):
    
    if request.method == "POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password =data.get('password')
        
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.error(request,"Username already taken.")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()

        messages.success(request,"User succesfully created.")
        return redirect('/register/')

    if request.user.is_authenticated:
        messages.info(request,"User Logged Out.")
        logout(request)
    return render(request, "register.html")