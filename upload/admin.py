from django.contrib import admin
from django.db import models

from .models import Upload


class UploadAdmin(admin.ModelAdmin):
    model = Upload
    list_display = ('file', 'upload_date')



admin.site.register(Upload, UploadAdmin)