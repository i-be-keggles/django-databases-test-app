from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class MongoDBModel(models.Model):
    # Fields for your MongoDB model
    film_id = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    release_year = models.IntegerField()
    language_id = models.IntegerField()
    original_language_id = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(decimal_places=2, max_digits=10)
    length = models.IntegerField()
    replacement_cost = models.DecimalField(decimal_places=2, max_digits=10)
    rating = models.CharField(max_length=20)
    special_features = models.CharField(max_length=100)
    last_update = models.CharField(max_length=50)
    category_id = models.IntegerField()
    name = models.CharField(max_length=100)