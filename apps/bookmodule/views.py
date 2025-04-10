from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
 return render(request, "bookmodule/index.html")

def list_books(request):
 return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')

def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def __getBooksList():
 book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
 book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
 book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
 return [book1, book2, book3]

def search_view(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        search_title = 'option1' in request.POST
        search_author = 'option2' in request.POST
        
        results = []
        for book in __getBooksList():
            title_match = search_title and keyword in book['title'].lower()
            author_match = search_author and keyword in book['author'].lower()
            
            if title_match or author_match:
                results.append(book)
        
        return render(request, 'books/html5/list/book_list.html', {'books': results})
    
    return render(request, 'books/html5/search/search.html')