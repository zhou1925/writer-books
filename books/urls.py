from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path(
        route='<int:pk>/', 
        view=views.BookDetailView.as_view(),
        name='detail'),
    path(
        route='<int:pk>/update/',
        view=views.BookUpdateView.as_view(),
        name='update'),
    path(
        route='mine/',
        view=views.MyBookList.as_view(),
        name='list'),
    path(
        route='create/',
        view=views.BookCreateView.as_view(),
        name='create_book'),
    path(
        route='<int:book_id>/chapter/<int:id>/update/',
        view=views.ChapterUpdateView.as_view(),
        name='chapter_update'),
    path(
        route='<int:book_id>/chapter/<int:pk>/',
        view=views.ChapterDetailView.as_view(),
        name='chapter_detail'),
    path(
        route='<int:book_id>/chapter/create/',
        view=views.chapterCreate,
        name='chapter_create')
]
