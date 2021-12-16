from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home_list'),
    # path('', views.book_upload, name='book_upload'),
    path('', views.data_upload, name='data'),
    path('results/', views.results, name='results'),
    # path('', views.HomeView.as_view(), name='home_list'),
]