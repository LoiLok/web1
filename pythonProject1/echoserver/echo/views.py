from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm

books = Book.objects.all()
print(books)

def homePageView(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'echo/base.html', {'books': books , 'request': request})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'echo/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'echo/book_form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'echo/book_confirm_delete.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    per_page = request.GET.get('per_page', 5)

    try:
        per_page = int(per_page)
    except (TypeError, ValueError):
        per_page = 5

    paginator = Paginator(books, per_page)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'echo/base.html', {'page_obj': page_obj,
        'paginator': paginator,
        'per_page': per_page})
