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
 path('books/lab9/task1', views.lab9_task1, name='lab9.task1'),
 path('books/lab9/task2', views.lab9_task2, name='lab9.task2'),
 path('books/lab9/task3', views.lab9_task3, name='lab9.task3'),
 path('books/lab9/task4', views.lab9_task4, name='lab9.task4'),
 path('init/sampledata', views.create_sample_data, name='create_sample_data'),
 path('lab9_part1/listbooks', views.list_books, name='list_books'),
 path('lab9_part1/addbook', views.add_book, name='add_book'),
 path('lab9_part1/editbook/<int:id>/', views.edit_book, name='edit_book'),
 path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),
 path('lab9_part2/listbooks', views.list_books_part2, name='list_books_part2'),
 path('lab9_part2/addbook', views.add_book_part2, name='add_book_part2'),
 path('lab9_part2/editbook/<int:id>/', views.edit_book_part2, name='edit_book_part2'),
 path('lab9_part2/deletebook/<int:id>/', views.delete_book_part2, name='delete_book_part2'),

]