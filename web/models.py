from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    organization_fk = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Task(models.Model): 
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=1000, null=True)
    date_posted = models.DateTimeField()
    date_finished = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=False)
    owner_fk = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        """String for representing the Model object."""
        return self.name