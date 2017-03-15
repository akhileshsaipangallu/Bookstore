# future
from __future__ import unicode_literals

# Django
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import reverse


class Publisher(models.Model):
    publisher_id = models.CharField(max_length=20, unique=True, null=False)
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    number_of_books = models.IntegerField(null=True, default=0)

    def get_absolute_url(self):
        return reverse(
            'publisher_details',
            kwargs={
                'publisher_id': self.publisher_id,
            }
        )

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    number_of_books = models.IntegerField(null=True, default=0)
    view_count = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse(
            'author_details',
            kwargs={
                'id': self.id,
            }
        )

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    book_id = models.CharField(max_length=20, unique=True, null=False)
    title = models.CharField(max_length=120)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True,
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, null=True, blank=True
    )
    price = models.FloatField()
    view_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)
        self.author.view_count += self.view_count
        self.author.save()

    def get_absolute_url(self):
        return reverse(
            'book_details',
            kwargs={
                'book_id': self.book_id,
            }
        )

    def __unicode__(self):
        return self.title


@receiver(post_save, sender=Book)
def update_book_count(sender, instance, **kwargs):
    instance.author.number_of_books = len(
        Book.objects.filter(author=instance.author)
    )
    instance.author.save()
    instance.publisher.number_of_books = len(
        Book.objects.filter(publisher=instance.publisher)
    )
    instance.publisher.save()
