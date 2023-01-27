from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def EmployeeView(request):
    form  = EmployeeForm()
    template_name = 'ClassApp/home.html'
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_url')
    context = {'form':form}
    return render(request, template_name, context)


def EmployeeDisplay(request):
    data = Employee.objects.all()
    template_name = 'ClassApp/display.html'
    context = {'data': data}
    return render(request, template_name, context)

def EmployeeUpdate(request,pk):
    data = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=data)
    template_name = 'ClassApp/home.html'
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        form.is_valid()
        form.save()
        return redirect('display_url')
    context = {'form':form}
    return render(request, template_name, context)


def EmployeeDelete(request, pk):
    data = Employee.objects.get(id=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('display_url')
    template_name = 'ClassApp/delete.html'
    context = {'data':data}
    return render(request, template_name, context)


