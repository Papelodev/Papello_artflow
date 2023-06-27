from django.db import models
from apps.usuarios.models import MyUser


class EmployeeProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    # Additional fields for employee profile
    employee_id = models.CharField(max_length=50 )
    department = models.CharField(max_length=100)
    # ...

class Task(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Additional fields for task
    status = models.CharField(max_length=50)
    due_date = models.DateField()
    # ...

class Review(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    reviewer = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, related_name='reviews')
    comments = models.TextField()
    # Additional fields for review
    rating = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    # ...

class Design(models.Model):
    designer = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, null=True, related_name='designs')
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Additional fields for design
    image = models.ImageField(upload_to='designs/')
    date_created = models.DateTimeField(auto_now_add=True)
    # ...
