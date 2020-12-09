from django.db import models
import random
import os

from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 3903459312)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'.format(new_filename= new_filename, ext = ext)
    return 'products/{new_filename}/{final_filename}'.format(new_filename = new_filename, final_filename = final_filename)

def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    return name, ext

class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)
