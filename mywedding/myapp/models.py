from django.db import models
from django.urls import reverse


# Create your models here.
class Year(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
         return reverse('myapp:allyear',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='product', blank=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

  #  def get_url(self):
   #     return reverse('shop:prodCatdetail',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)
