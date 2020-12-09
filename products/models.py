from django.db import models
import random
import os


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 3903459312)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'.format(new_filename= new_filename, ext = ext)
    return 'products/{new_filename}/final_filename}'.format(new_filename = new_filename, final_filename = final_filename)

def get_filename_ext(filename):
    base_name = os.path.basename(filpath)
    name, ext = os.path.splitext(filepath)
    return name, ext

# Create your models here.
class Product(models.Model):
    title           = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title