from django.db import models

from django.urls import reverse


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genres = models.TextField(max_length=500)

    # def __str__(self):
    #     return self.title


class Upload(models.Model):
    file = models.FileField(upload_to='csv/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file

    def get_absolute_url(self):
        return reverse('upload-detail', args=[str(self.id)])



    # title = models.CharField(max_length=50)
    # author = models.CharField(max_length=50)
    # num_rating = models.IntegerField()
    # num_reviews = models.IntegerField()
    # avg_rating,num_pages = models.FloatField(),models.IntegerField()
    # original_publish_year = models.IntegerField()
    # series = models.CharField(max_length=50)
    # minmax_norm_ratings = models.FloatField(),models.FloatField()
    # mean_norm_ratings = models.FloatField()
    # genres = models.CharField(max_length=50)
    # award = models.CharField(max_length=50)


# Django request/response cycle
# VMT: View, Model, Template
# URL -> View -> Model -> Template -> HttpResponse