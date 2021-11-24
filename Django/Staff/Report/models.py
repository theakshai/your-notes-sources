from django.db import models

# Create your models here.
'''
1. Staff Id
2. Staff Name
3. Staff Designation
4. Staff Salary
'''
class Employee_Details(models.Model):
	staff_id = models.IntegerField()
	staff_name = models.TextField()
	staff_designation = models.CharField(max_length=50)
	staff_salary = models.IntegerField()
