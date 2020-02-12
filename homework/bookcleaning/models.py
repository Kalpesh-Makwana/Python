from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    username=models.CharField('username',max_length=12)
    contact = models.CharField('contact',max_length=12,unique=True)
    first_name  = models.CharField('first_last',max_length=30,blank=True)
    last_name   = models.CharField('Last_last',max_length=30,blank=True)
    is_cleaner  = models.BooleanField('cleaner', default=False)

    USERNAME_FIELD = 'contact'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.contact)

    def get_absolute_url(self):
        return reverse("bookcleaning:profile", kwargs={"pk": self.pk})

class City(models.Model):
    name=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return str(self.name)

class Cleaner(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    quality_score=models.FloatField(default=0)
    city=models.ForeignKey(City,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user.first_name)

