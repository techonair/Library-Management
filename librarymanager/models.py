from django.db import models
from django.contrib.auth.models import AbstractUser

"""
class AdminUser(models.Model):
    username = models.OneToOneField(User, max_length=50, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)
    image = models.ImageField(upload_to="", blank=True, default='avatar.svg')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return 'status: Admin,' + str(self.username) + ":" + str(self.email)
"""

class Student(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    roll_no = models.CharField(max_length=50, unique=True)
    standard = models.CharField(max_length=20)
    phone = models.CharField(max_length=10, unique=True, blank=True)
    image = models.ImageField(upload_to="", blank=True, default='avatar.svg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.username) + ":" + str(self.email) + "," + str(self.roll_no) + "," + str(self.standard)

class Book(models.Model):
    book_name = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    ISBN = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.book_name) + ":" + str(self.author) + "," + str(self.category) + "," + str(self.ISBN)