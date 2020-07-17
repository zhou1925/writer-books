from django.shortcuts import render
from django.views.generic import DetailView

from .models import Book


class BookDetailView(DetailView):
    model = Book

    async def __call__(self):
        return super().__call__(self)


