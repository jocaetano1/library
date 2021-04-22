from django.db import models

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    subtitle = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    pub_date = models.DateField(null=True)

    class Meta:
        pass
    
    def __str__(self):
        return self.title