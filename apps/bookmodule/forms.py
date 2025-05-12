from tkinter import Image
from django import forms
from .models import Address, Book, Student, Image

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'description']