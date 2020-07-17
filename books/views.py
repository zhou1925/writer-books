from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView, View

from asgiref.sync import sync_to_async

from .models import Book


class AsyncViewMixin:
    async def __call__(self):
        return super().__call__(self)


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

    def get_object(self, queryset=None):
        return get_object_or_404(Book, id=self.kwargs['pk'],
        creator=self.request.user)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = (
        'title',
        'description',
        'contributors',
    )

    def get_object(self, queryset=None):
        return get_object_or_404(Book, id=self.kwargs['pk'],
        creator=self.request.user)

