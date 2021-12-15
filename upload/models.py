from django.db import models

from django.urls import reverse



# class Books(models.Model):
#     title = models.CharField(("title"), max_length=200)
#     author = models.CharField(("author"), max_length=200)
#     genres = models.TextField(("genres"), max_length=500)

#     def __str__(self):
#         return self.title


class BooksComplete(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    num_rating = models.IntegerField()
    num_reviews = models.IntegerField()
    avg_rating = models.FloatField()
    num_pages = models.IntegerField()
    original_publish_year = models.IntegerField()
    award = models.CharField(max_length=50)



    def __str__(self):
        return self.title


# class Customers(models.Model):
#     file = models.FileField(upload_to='csv/')
#     upload_date = models.DateTimeField(auto_now_add=True)
#     title = models.ForeignKey(BooksComplete, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.file

#     def get_absolute_url(self):
#         return reverse('upload-detail', args=[str(self.id)])




# Django request/response cycle
# VMT: View, Model, Template
# URL -> View -> Model -> Template -> HttpResponse