from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .forms import Employee
from .models import Employee_details

# Request of url = ''

def home(request):
	return render(request, 'home.html')

def employeeDetails(request):
	if request.method == 'POST':
		# Id = request.POST["staff_id"]
		# Name = request.POST["staff_name"]
		# Designation = request.POST["designation"]
		# Salary = request.POST["salary"]

		# form = Employee(staff_id = Id, staff_name = Name, designation = Designation, salary= Salary )
		form = Employee(request.POST)
		if form.is_valid():
			form.save()
			print(form)
			return HttpResponseRedirect('/added/')
	else:
		form = Employee()
	return render(request, 'employeeForm.html',{'form':form})

def displayDetails(request):
	employee_list = Employee_details.objects.all()
	return render(request, 'display.html',{'employee_list':employee_list} )

def thanks(request):
	return render(request, 'thanks.html')