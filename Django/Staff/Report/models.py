from django.db import models
# ['staff_id', 'staff_name', 'designation', 'salary']
class Employee_details(models.Model):

	staff_id = models.CharField(max_length=100)

	staff_name = models.CharField(max_length=100)

	designation = models.CharField(max_length=100)

	salary = models.CharField(max_length=100)

	def __str__(self):
		return self.staff_name