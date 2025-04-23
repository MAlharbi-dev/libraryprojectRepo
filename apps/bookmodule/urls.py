from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.viewbook"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('search/', views.search_view, name='search'),
 path('simple/query', views.simple_query, name='simple-query'),
 path('complex/query/', views.complex_query, name='complex-query'),
 path('lab8/task1/', views.task1, name='lab8-task1'),
 path('lab8/task2/', views.task2, name='lab8-task2'),
 path('lab8/task3/', views.task3, name='lab8-task3'),
 path('lab8/task4/', views.task4, name='lab8-task4'),
 path('lab8/task5/', views.task5, name='lab8-task5'),
 path('lab8/student-stats/', views.student_stats, name='student-stats'),
]