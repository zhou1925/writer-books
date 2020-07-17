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
]
