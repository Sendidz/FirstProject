from django.db import models

class Article(models.Model):
    name = models.CharField(max_length = 24)
    price = models.CharField(max_length = 10)
    page = models.CharField(max_length = 4)
    auth = models.CharField(max_length = 24)
    image = models.ImageField(upload_to= 'static/images/article/')

