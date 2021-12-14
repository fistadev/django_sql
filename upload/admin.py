from django.contrib import admin
from django.db import models
from django.contrib.admin.decorators import register
from .models import *


class BooksAdmin(admin.ModelAdmin):
    model = Books
    list_display = ('title',)
    list_filter = ('genres',)


admin.site.register(Books, BooksAdmin)
# admin.site.register(Upload)