from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from pages.forms import BookForm, FeedbackForm
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


def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save()
        messages.success(request, 'Книга успешно добавлена.')
        return redirect('book_detail', pk=book.pk)

    context = {
        'title': 'Добавить новую книгу',
        'form': form,
        'button_text': 'Сохранить',
    }
    return render(request, 'pages/book_form.html', context)


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        book = form.save()
        messages.success(request, 'Книга успешно обновлена.')
        return redirect('book_detail', pk=book.pk)

    context = {
        'title': 'Редактировать книгу',
        'form': form,
        'button_text': 'Обновить',
        'book': book,
    }
    return render(request, 'pages/book_form.html', context)


def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            messages.success(request, 'Сообщение успешно отправлено. Спасибо за обратную связь!')
            return redirect('home')
    else:
        form = FeedbackForm()

    context = {
        'title': 'Контакты',
        'form': form,
    }
    return render(request, 'pages/contact.html', context)
