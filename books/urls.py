from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail' ),
]
