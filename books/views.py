from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author
from .forms import BookForm, AuthorForm

def home(request):
    authors = Author.objects.all()
    return render(request, 'books/index.html', {'authors': authors})


def book_list(request):
    author_id = request.GET.get('author')
    search_query = request.GET.get('q')

    books = Book.objects.all()

    if author_id:
        books = books.filter(author__id=author_id)
    if search_query:
        books = books.filter(title__icontains=search_query)

    authors = Author.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'authors': authors})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = author.book_set.all()
    return render(request, 'authors/authors_detail.html', {'author': author, 'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = AuthorForm()
    return render(request, 'authors/author_form.html', {'form': form})



def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'authors/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('author_list')
    return render(request, 'authors/author_confirm_delete.html', {'author': author})


