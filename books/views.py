from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from asgiref.sync import sync_to_async

from .models import Book


class BookDetailView(DetailView):
    model = Book

    def get_object(self, queryset=None):
        return sync_to_async(super().get_object(queryset))

    async def __call__(self):
        return super().__call__(self)


