from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')
    name = models.CharField('SubCategory name', max_length=60)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'

class Product(models.Model):

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=80)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Product image', upload_to='images')
    logo = models.ImageField('Product logo', upload_to='images', blank=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    