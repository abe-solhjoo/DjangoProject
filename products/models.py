from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse


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
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    active = models.BooleanField(default=False)

    def get_absolute_url(self):
        # return f"/products/{self.slug}"
        return reverse("products:detail", kwargs={"slug": self.slug})

    objects = ProductManager()

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
