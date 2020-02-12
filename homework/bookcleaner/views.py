from django.shortcuts import render
from django.views.generic import View,ListView
from .forms import BookCleanerForm
from .models import BookingCleanerModel
from bookcleaning.models import Cleaner,City
from django.http import HttpResponse
# Create your views here.

class BookCleanerView(View):
    def get(self,request):
        form=BookCleanerForm()
        return render(request,'bookcleaner.html',{'form':form})
    
    def post(self,request):
        form=BookCleanerForm(request.POST)
        if form.is_valid():
            city=form.cleaned_data.get('city')
            timeslot=form.cleaned_data.get('timeslot')
            date=form.cleaned_data.get('date')
            booked=BookingCleanerModel.objects.filter(city__name=city,timeslot=timeslot,date=date)
            # cleaner=Cleaner.objects.filter(city__name=city)
            cleaner=Cleaner.objects.filter(city__name=city).exclude(user__in=[x.cleaner.user for x in booked]).exclude(user=request.user)
        return render(request,'bookcleaner.html',{'form':form,'tiemeslot':timeslot,'cleaner':cleaner,'date':date})

class BookOrderView(View):
    def post(self,request):
        data=request.POST.copy()
        print(data)
        city=City.objects.get(id=data['city'])
        cleaner=Cleaner.objects.get(id=data['cleaner'])
        obj=BookingCleanerModel.objects.create(user=request.user,cleaner=cleaner,city=city,date=data['date'],timeslot=data['timeslot'])
        data=BookingCleanerModel.objects.filter(user=request.user)
        return render(request,'afterbooking.html',{'data':data})
        
class BookingListView(ListView):
    model=BookingCleanerModel
    template_name = 'mybookings.html' 
    
    def get_queryset(self):
        return BookingCleanerModel.objects.filter(user=self.request.user)

class CleanerListView(ListView):
    model=BookingCleanerModel
    template_name = 'cleanerlist.html' 
    
    def get_queryset(self):
        return BookingCleanerModel.objects.filter(cleaner__user=self.request.user)