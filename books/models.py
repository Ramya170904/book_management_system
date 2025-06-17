from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ])

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
