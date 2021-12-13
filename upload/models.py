from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



# Django request/response cycle
# URL -> View -> Model -> Template -> HttpResponse