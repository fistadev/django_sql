from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home_list'),
    # path('', views.book_upload, name='book_upload'),
    path('results/', views.results, name='results'),
    path('data/', views.plot_view, name='data'),
    path('', views.HomeView.as_view(), name='home_list'),
]