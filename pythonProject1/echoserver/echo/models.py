from django.db import models


class Book(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=50)
    price = models.IntegerField(default=0)


    class Meta:
        db_table = 'books'
        managed = False

    def __str__(self):
        return self.title