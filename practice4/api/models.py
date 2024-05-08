from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    used = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=200)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart_Item(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    repeated = models.BooleanField(default=False)
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    liked = models.ForeignKey(Category, on_delete=models.CASCADE)

class ProductQuerySet(models.QuerySet):
    def used_product(self):
        return self.filter(used= True)
    def not_used_product(self):
        return self.filter(used=False)

class CartQuerySet(models.QuerySet):
    def repeated(self):
        return self.filter(repeated=True)
    
    def not_repeated(self):
        return self.filter(repeated=False)


class CartManager(models.Manager):
    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)

    def repeatedItems(self):
        return self.get_queryset().repeated()
    
    def notRepeatedItems(self):
        return self.get_queryset().not_repeated()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def usedItems(self):
        return self.get_queryset().used_product()
    
    def not_usedItems(self):
        return self.get_queryset().not_used_product()
