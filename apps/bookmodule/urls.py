from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.viewbook"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('search/', views.search_view, name='search'),

]