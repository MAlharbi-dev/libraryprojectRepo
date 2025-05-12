from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Address, Book, Course, Department, Student, Card
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .forms import AddressForm, BookForm, ImageForm, StudentForm


# samples 

def create_sample_data(request):
    # Create Address
    addr = Address.objects.create(city="Riyadh")

    # Create Card
    card = Card.objects.create(card_number=123456)

    # Create Department
    dept = Department.objects.create(name="Computer Science")

    # Create Courses
    c1 = Course.objects.create(title="Algorithms", code=101)
    c2 = Course.objects.create(title="Databases", code=102)

    # Create Student
    student = Student.objects.create(
        name="Ahmed",
        age=21,
        address=addr,
        card=card,
        department=dept
    )
    student.courses.set([c1, c2])

    return HttpResponse("Sample data created successfully.")

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

def simple_query(request):
    # This filters all books with 'and' in the title (case-insensitive)
    mybooks = Book.objects.filter(title__icontains='and')
    
    return render(request, 'bookmodule/list_books.html', {'books': mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull =
False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/list_books.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8/task1.html', {'books': books})

def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task2.html', {'books': books})

def task3(request):
    books = Book.objects.filter(
        ~Q(edition__gt=3) & 
        ~(Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8/task3.html', {'books': books})

def task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8/task4.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8/task5.html', {'stats': stats})

def student_stats(request):
    cities = Address.objects.annotate(
        student_count=Count('student')
    ).order_by('-student_count')
    return render(request, 'bookmodule/student_stats.html', {'cities': cities})

def lab9_task1(request):
    departments = Department.objects.all()

    data = []
    for dept in departments:
        student_count = dept.students.count()  # using related_name='students'
        data.append({'name': dept.name, 'count': student_count})

    return render(request, 'bookmodule/lab9_task1.html', {'departments': data})

def lab9_task2(request):
    courses = Course.objects.annotate(
        student_count=Count('students')
    ).order_by('title')
    return render(request, 'bookmodule/lab9_task2.html', {'courses': courses})

def lab9_task3(request):
    departments = Department.objects.annotate(
        oldest_student_id=Min('students__id')
    ).filter(oldest_student_id__isnull=False)
    
    oldest_students = []
    for dept in departments:
        student = Student.objects.filter(
            department=dept,
            id=dept.oldest_student_id
        ).first()
        if student:
            oldest_students.append({
                'department': dept,
                'student': student
            })
    
    return render(request, 'bookmodule/lab9_task3.html', {'oldest_students': oldest_students})

def lab9_task4(request):
    departments = Department.objects.annotate(
        student_count=Count('students')
    ).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/lab9_task4.html', {'departments': departments})

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return redirect('list_books')
    return render(request, 'add_book.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('list_books')
    return render(request, 'edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books')

def list_books_part2(request):
    books = Book.objects.all()
    return render(request, 'list_books_part2.html', {'books': books})

def add_book_part2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm()
    return render(request, 'add_book_part2.html', {'form': form})

def edit_book_part2(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books_part2')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book_part2.html', {'form': form})

def delete_book_part2(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books_part2')

# List all students
def list_students(request):
    students = Student.objects.all()
    return render(request, 'students/list_students.html', {'students': students})

# Add a new student
def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        address_form = AddressForm(request.POST)
        if student_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            student = student_form.save()
            student.addresses.add(address)
            return redirect('list_students')
    else:
        student_form = StudentForm()
        address_form = AddressForm()
    return render(request, 'students/add_student.html', {'student_form': student_form, 'address_form': address_form})

# Edit a student's data
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student_form = StudentForm(request.POST, instance=student)
        address_form = AddressForm(request.POST)
        if student_form.is_valid() and address_form.is_valid():
            address = address_form.save()
            student.addresses.add(address)
            student_form.save()
            return redirect('list_students')
    else:
        student_form = StudentForm(instance=student)
        address_form = AddressForm()
    return render(request, 'students/edit_student.html', {'student_form': student_form, 'address_form': address_form})
# Delete a student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')

def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageForm()
    return render(request, 'students/add_image.html', {'form': form})