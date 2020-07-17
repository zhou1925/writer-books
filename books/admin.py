from django.contrib import admin

from .models import Book, ContributorType, Chapter


admin.site.register(Book)
admin.site.register(ContributorType)
admin.site.register(Chapter)