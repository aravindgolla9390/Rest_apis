from django.db import models

class Book(models.Model):
    book_name=models.CharField(max_length=200)
    book_price=models.IntegerField()
    book_authour=models.CharField(max_length=200)
    
    def __str__(self):
        return self.book_name


class Fileuploading(models.Model):
    file_name=models.CharField(max_length=200)
    file=models.FileField()

    def __str__(self):
        return self.file_name
        