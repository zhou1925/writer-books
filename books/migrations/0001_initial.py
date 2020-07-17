# Generated by Django 3.0.8 on 2020-07-17 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
            ],
        ),
        migrations.CreateModel(
            name='ContributorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250, verbose_name='Type')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Book')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='contributors',
            field=models.ManyToManyField(related_name='book_authors', through='books.ContributorType', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]