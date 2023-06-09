from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=35)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=35)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title



STARS_CHOICES = (
    (1, '*'),
    (2, 2 * '**'),
    (3, 3 * '***'),
    (4, 4 * '****'),
    (5, 5 * '*****')
)

class Review(models.Model):
    text = models.TextField(max_length=310)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    stars = models.IntegerField(default=5)

    def __str__(self):
        return self.text

