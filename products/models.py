from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
    
def image_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    return f'static/images/products/{instance.pk}.{ext}'

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=image_upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CATEGORY_CHOICE = (
        ('shirt','shirt'),
        ('t-shirt','t-shirt'),
        ('trousers','trousers'),
        ('jacket','jacket'),
        ('shorts','shorts'),
        ('dress','dress'),
        ('jeans','jeans'),
        ('others','others')
    ) 
    category = models.CharField(choices=CATEGORY_CHOICE,max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        ordering = ['category','price']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Save the object first to generate the primary key if it's not set 
        image = self.image
        self.image = None
        super().save(*args, **kwargs)
        # Call save again to ensure the image is saved with the primary key as name
        self.image = image
        super(Products, self).save(*args, **kwargs)

class Stock(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    small = models.IntegerField()
    medium = models.IntegerField()
    large = models.IntegerField()

    def __str__(self):
        return str(self.product) + "_stock"