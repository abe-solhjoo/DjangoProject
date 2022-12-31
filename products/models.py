from django.db import models


class ProductManager(models.Manager):
    def get_featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, productId):
        qs = self.get_queryset().filter(id=productId)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        return self.title
