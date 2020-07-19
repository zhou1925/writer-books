from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ContributorType(models.Model):
    user = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL)
    book = models.ForeignKey("Book", null=True, on_delete=models.SET_NULL)
    type = models.CharField("Type", max_length=250)


class Book(models.Model):
    title = models.CharField("Title", max_length=250)
    description = models.TextField()
    creator = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="book_creator"
    )
    contributors = models.ManyToManyField(
        User, related_name="book_authors", through=ContributorType
    )

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    title = models.CharField("Title of Chapter", max_length=250)
    body = models.TextField("Body")

    def get_absolute_url(self):
        return reverse(
            "books:chapter_detail",
            kwargs={"pk": self.pk, 'book_id': self.book_id})

    def __str__(self):
        return self.title
