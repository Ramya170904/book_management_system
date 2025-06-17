

from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'published_date', 'author', 'description']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age', 'gender']  