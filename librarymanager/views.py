from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def student_login(request):
    return render(request, 'student_login.html')

def add_book(request):
    return render(request, 'add_book.html')

def get_books(request):
    return render(request, 'get_book.html')

def update_book(request, pk):
    return render(request, 'update_book.html')

def delete_book(request, pk):
    return render(request, 'delete_book.html')