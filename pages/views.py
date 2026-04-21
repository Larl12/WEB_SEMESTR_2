from django.shortcuts import get_object_or_404, render

from pages.models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'title': 'Сервис обмена книгами',
        'welcome_text': 'Добро пожаловать на наш лучший сайт для обмена книгами.',
        'books': books,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {
        'title': 'О проекте',
        'description': 'Books Exchange — это площадка, где книги находят новых читателей.',
    }
    return render(request, 'pages/about.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {
        'title': book.title,
        'book': book,
    }
    return render(request, 'pages/book_detail.html', context)
