from django.shortcuts import render

def index(request):
    context = {
        'title': 'Сервис обмена книгами',
        'welcome_text': 'Добро пожаловать на наш лучший сайт для обмена книгами.',
    }
    return render(request, 'pages/index.html', context)


def about(request):
    context = {
        'title': 'О проекте',
        'description': 'Books Exchange — это площадка, где книги находят новых читателей.',
    }
    return render(request, 'pages/about.html', context)
