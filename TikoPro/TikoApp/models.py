from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



#user profile models
class Profile(models.Model):
    photo=models.ImageField(upload_to='avatars/',blank=True,null=True)
    bio=models.TextField(max_length=250)
    user=models.ForeignKey(User)
    email=models.EmailField(null=True, blank=True, unique=True)
    phone_number=models.PositiveIntegerField(default=+254720000000)
    update_time = models.DateTimeField(auto_now_add=True, null=True)



# events category model/fileds
class EventType(models.Model):
    name=models.CharField(max_length=150,)
    
    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name



class Event(models.Model):
    eventtype=models.ForeignKey(EventType,related_name='events',on_delete=models.CASCADE)
    name=models.CharField(max_length=100,)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    available=models.BooleanField(default=True)
    tickets= models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='gallery/',blank=True,null=True)
    location = models.CharField(max_length=30, blank=True)
    Event_date=models.DateField()
    Event_time=models.TimeField()
    tags = models.ManyToManyField(Tags)


    def __str__(self):
        return self.name
        



#creat user profile on register 
def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)