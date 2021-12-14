from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *


# class UploadAdmin(admin.ModelAdmin):
#     model = Upload
#     list_display = ('file', 'upload_date')


admin.site.register(Books)