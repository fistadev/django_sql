from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path(r'^media/csv/$', views.upload_csv, name='upload_csv'),
]