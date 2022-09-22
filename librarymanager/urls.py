from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('admin-login/', views.admin_login,  name='admin-login'),
    path('student-login/', views.student_login,  name='student-login'),
    path('get-book/', views.get_books,  name='get-books'),
    path('add-book/', views.add_book,  name='add-book'),
    path('update-book/<str:pk>', views.update_book,  name='update-book'),
    path('delete-book/<str:pk>', views.delete_book,  name='delete-book'),
]