from django.contrib import admin
from django.urls import path

from pages.views import about, book_detail, contact, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('books/<int:pk>/', book_detail, name='book_detail'),
    path('contact/', contact, name='contact'),
]
