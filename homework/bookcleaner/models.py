from django.db import models
from bookcleaning.models import User,Cleaner,City
# Create your models here.

class BookingCleanerModel(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    cleaner=models.ForeignKey(Cleaner,null=True,on_delete=models.SET_NULL)
    city=models.ForeignKey(City,null=True,on_delete=models.SET_NULL)
    date=models.DateField()
    timeslot=models.IntegerField(null=True)

    def __str__(self):
        return str(self.cleaner)
    
    def get_absolute_url(self):
        return reverse('bookcleaner:bookinglist',kwargs={'pk':self.pk})
