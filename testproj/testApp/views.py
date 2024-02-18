from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

def home(request):
    qs = Employee.objects.all()
    context = {'qs':qs}
    return render(request, 'testApp/home.html', context)


def addEmployee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/success/')
    form = EmployeeForm()
    return render(request,'testApp/submit.html',{'form':form})


def editEmp(request, pk):
    isinstance = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=isinstance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('updated successfully')
    
    return render(request, 'testApp/edit.html', {'form':form})


def delete_emp(request,pk):
    qs = get_object_or_404(Employee,pk=pk)
    if request.method == 'POST':
        qs.delete()
        return HttpResponse('/success/')
    context = {}
    return render(request, 'testApp/delete.html', context)
    
