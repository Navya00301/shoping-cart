from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
from django.contrib.auth.models import User

class Cart(models.Model):
        user= models.ForeignKey(User, on_delete=models.CASCADE)

        def total_price(self):
            return sum(item.total_price() for item in self.cartitem_set.all())
        
class Cartitem(models.Model):
        cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        quantity=models.PositiveBigIntegerField(default=1)

        def total_price(self):
              return self.product.price * self.quantity
         

