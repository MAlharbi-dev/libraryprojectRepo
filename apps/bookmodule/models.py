from django.db import models
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)
    
class Address(models.Model):
    city = models.CharField(max_length=100)
    
class Card(models.Model):
    card_number = models.IntegerField()
    def delete(self, *args, **kwargs):
            if hasattr(self, 'student'):
                raise ValidationError("Cannot delete a card linked to a student!")
            super().delete(*args, **kwargs)
    
class Department(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
                
 
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    card = models.OneToOneField(
        Card,
        on_delete=models.PROTECT,  # Prevents card deletion if linked
        related_name='student'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,  # This makes sure students are deleted when department is deleted
        related_name='students'
    )
    courses = models.ManyToManyField(Course, related_name='students')



