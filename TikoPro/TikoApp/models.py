from django.db import models
from django.contrib.auth.models import User



#user profile models
class Profile(models.Model):
    photo=models.ImageField(upload_to='avatars/',blank=True,null=True)
    bio=models.TextField(max_length=250)
    user=models.ForeignKey(User)
    update_time = models.DateTimeField(auto_now_add=True, null=True)



# events category model/fileds
class Category(models.Model):
    name=models.CharField(max_length=150,)

class Event(models.Model):
    category=models.ForeignKey(Category,related_name='events',on_delete=models.CASCADE)
    name=models.CharField(max_length=100,)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    tickets= models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='gallery/',blank=True,null=True)
    Event_date=models.DateField()
    Event_time=models.TimeField()
