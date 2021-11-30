from django import forms
from django.forms import ModelForm 

from .models import Employee_details

class Employee(ModelForm):

	class Meta:

		model = Employee_details
		fields = ['staff_id', 'staff_name', 'designation', 'salary']
 