from django.contrib import admin
from django.urls import path

from pages.views import about, book_create, book_detail, book_update, contact, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('books/create/', book_create, name='book_create'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('books/<int:pk>/edit/', book_update, name='book_update'),
    path('contact/', contact, name='contact'),
]
