from django.contrib import admin
from pages.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'copies_available', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    fields = ('title', 'description', 'copies_available', 'created_at')
