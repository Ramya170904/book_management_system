from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/add/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # Author URLs
    path('', views.home, name='home'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/add/', views.author_create, name='author_create'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
    path('authors/<int:pk>/update/', views.author_update, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
]
