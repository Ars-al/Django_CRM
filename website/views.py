from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddHrRecordForm, AddEmployeeRecordForm
from .models import Record, HrRecord, EmployeeRecord

def home(request):
    records = Record.objects.all()
    
    # check if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "Loggin in error, Please try again...")
            return redirect('home')
        
    else:
        return render(request, 'home.html', {'records':records})



def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully Logged out!")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully Registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        # see records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be Logged In to view records!")
        return redirect('home')
    
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        # delete record
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must be Logged In to delete record!")
        return redirect('home')
    
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully!")
                return redirect('home')
        return render(request, 'add_record.html', {"form":form})
    else:
        messages.success(request, "You must be Logged In!")
        return redirect('home')
    
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be Logged In!")
        return redirect('home')
    
#  HR panel and Record
    
def hr_panel(request):
    hr_records = HrRecord.objects.all()
    if request.user.is_authenticated:
        # see records
        return render(request, 'hr_panel.html', {'hr_records':hr_records})
    else:
        messages.success(request, "You must be Logged In to view HR records!")
        return redirect('home')
    
    
def hr_record_view(request, pk):
    if request.user.is_authenticated:
        hr_record_view = HrRecord.objects.get(id=pk)
        return render(request, 'hr_record_view.html', {'hr_record_view':hr_record_view})
    else:
        messages.success(request, "You must be Logged In to view HR records!")
        return redirect('home')
    
    
def add_hr_record(request):
    form = AddHrRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully!")
                return redirect('hr_panel')
        return render(request, 'add_hr_record.html', {"form":form})
    else:
        messages.success(request, "You must be Logged In!")
        return redirect('home')
    

def update_hr_record(request, pk):
    if request.user.is_authenticated:
        current_record = HrRecord.objects.get(id=pk)
        form = AddHrRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('hr_panel')
        return render(request, 'update_hr_record.html', {'form':form})
    else:
        messages.success(request, "You must be Logged In!")
        return redirect('home')
    
    
def delete_hr_record(request, pk):
    if request.user.is_authenticated:
        # delete record
        delete_it = HrRecord.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('hr_panel')
    else:
        messages.success(request, "You must be Logged In to delete record!")
        return redirect('home')
    
# Employee panel and Record    

def employee_panel(request):
    employee_records = EmployeeRecord.objects.all()
    if request.user.is_authenticated:
        # see records
        return render(request, 'employee_panel.html', {'employee_records':employee_records})
    else:
        messages.success(request, "You must be Logged In to view HR records!")
        return redirect('home')
    
    
def employee_record_view(request, pk):
    if request.user.is_authenticated:
        employee_record_view = EmployeeRecord.objects.get(id=pk)
        return render(request, 'employee_record_view.html', {'employee_record_view':employee_record_view})
    else:
        messages.success(request, "You must be Logged In to view HR records!")
        return redirect('home')
    
def add_employee_record(request):
    form = AddEmployeeRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added Successfully!")
                return redirect('employee_panel')
        return render(request, 'add_employee_record.html', {"form":form})
    else:
        messages.success(request, "You must be Logged In!")
        return redirect('home')
    
    
def update_employee_record(request, pk):
    if request.user.is_authenticated:
        current_record = EmployeeRecord.objects.get(id=pk)
        form = AddEmployeeRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect('employee_panel')
        return render(request, 'update_employee_record.html', {'form':form})
    else:
        messages.success(request, "You must be Logged In!")
        return redirect('home')
    
    
def delete_employee_record(request, pk):
    if request.user.is_authenticated:
        # delete record
        delete_it = EmployeeRecord.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('employee_panel')
    else:
        messages.success(request, "You must be Logged In to delete record!")
        return redirect('home')