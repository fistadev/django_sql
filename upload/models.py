from django.db import models

from django.urls import reverse



class Upload(models.Model):
    file = models.FileField(upload_to='csv/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

    def get_absolute_url(self):
        return reverse('upload-detail', args=[str(self.id)])





# Django request/response cycle
# VMT: View, Model, Template
# URL -> View -> Model -> Template -> HttpResponse