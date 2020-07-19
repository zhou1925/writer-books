from functools import cached_property

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, UpdateView, View, ListView, CreateView

from asgiref.sync import sync_to_async

from .models import Book, Chapter
from .forms import ChapterCreateForm

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

class MyBookList(LoginRequiredMixin, ListView):
    model = Book
    
    def get_objects(self, queryset=None):
        return Book.objects.filter(book_creator=self.request.user)


class ChapterDetailView(LoginRequiredMixin, DetailView):
    model = Chapter

    def get_object(self, queryset=None):
        try:
            return Chapter.objects.get(
                book__creator=self.request.user,
                book_id=self.kwargs['book_id'],
                id=self.kwargs['pk']
            )
        except Chapter.DoesNotExist:
            raise Http404


class ChapterUpdateView(LoginRequiredMixin, UpdateView):
    model = Chapter

    def get_object(self, queryset=None):
        try:
            return Chapter.objects.get(
                book_creator=self.request.user,
                book_id=self.kwargs['book_id'],
                id=self.kwargs['pk']
            )
        except Chapter.DoesNotExist:
            raise Http404


class ChapterCreateView(LoginRequiredMixin, CreateView):
    model = Chapter
    fields = ('title', 'body')

    def get_success_url(self):
        return self.book.get_absolute_url()

    @cached_property
    def book(self):
        return get_object_or_404(
            Book, id=self.kwargs['book_id'], creator=self.request.user
        )

    def get_object(self, queryset=None):
        try:
            return Chapter.objects.get(
                book_creator=self.request.user,
                book_id=self.kwargs['book_id'],
                id=self.kwargs['pk']
            )
        except Chapter.DoesNotExist:
            raise Http404
    
    def form_valid(self, form):
        chapter = form.save(commit=False)
        chapter.book = self.book
        chapter.save()
        return chapter.get_absolute_url()


def chapterCreate(request, book_id):
    book = get_object_or_404(Book, id=book_id, creator=request.user)

    new_chapter = None
    if request.method == 'POST':
        chapter_form = ChapterCreateForm(data=request.POST)
        if chapter_form.is_valid():
            new_chapter = chapter_form.save(commit=False)
            new_chapter.book = book

            new_chapter.save()
            return redirect(reverse('books:detail', kwargs={'pk': book_id}))

    else:
        chapter_form = ChapterCreateForm()

    return render(request, 'books/chapter_form.html', {'book':book, 'chapter_form': chapter_form})

    


