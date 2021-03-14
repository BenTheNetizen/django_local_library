# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:30:59 2021

@author: benis
"""


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    #the URL special syntax <int:pk> passes a value to the view as 'pk' but this value must be an 'int'
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

]
