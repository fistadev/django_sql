from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('', views.HomeView.as_view(), name='home_list'),
    # path(r'^media/csv/$', views.upload_csv, name='upload_csv'),
]