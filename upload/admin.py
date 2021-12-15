from django.contrib import admin
from django.db import models
from django.contrib.admin.decorators import register
from .models import *


# class BooksAdmin(admin.ModelAdmin):
#     model = Books
#     list_display = ('title',)
#     list_filter = ('genres',)


class CompleteBooksAdmin(admin.ModelAdmin):
    model = BooksComplete
    list_display = ('title', 'author', 'original_publish_year', 'avg_rating')
    list_filter = ('original_publish_year', )


# admin.site.register(Books, BooksAdmin)
admin.site.register(BooksComplete, CompleteBooksAdmin)
# admin.site.register(Upload)

