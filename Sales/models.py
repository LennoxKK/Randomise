from itertools import product
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateField, DateTimeField
# Create your models here.

PRODUCT_CHOICES=(
    ('TV',"tv"),
    ('IPAD',"ipad"),
    ("PLAYSATTION",'playstation')

)
class Sales(models.Model):
    product=models.CharField(max_length=11,choices=PRODUCT_CHOICES)
    salesman=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    total=models.FloatField(blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}--{self.quantity}"

    def save(self,*args, **kwargs):
        price=None
        if self.product=='TV':
            price=599.99
        elif self.product=="IPAD":
            price=400.00
        elif self.product=="PLAYSTATION":
            price=464.99
        else:
            pass
        self.total=price*self.quantity
        super().save(*args,**kwargs)
