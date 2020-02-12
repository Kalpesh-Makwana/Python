from django import forms
from bookcleaning.models import City
from .models import BookingCleanerModel
from django.utils import timezone

slots=(
    (1,'10:00 - 11:00'),
    (2,'11:00 - 12:00'),
    (3,'12:00 - 1:00'),
    (4,'2:00 - 3:00'),
    (5,'3:00 - 4:00'),
    (6,'4:00 - 5:00'),
    (7,'5:00 - 6:00'),
    (8,'6:00 - 7:00'),
)

class BookCleanerForm(forms.Form):
    city=forms.ModelChoiceField(label="Select City",queryset=City.objects.all())
    timeslot=forms.IntegerField(widget=forms.Select(choices=slots))
    date=forms.DateField(widget=forms.DateTimeInput(attrs={
        'class': 'form-control datetimepicker-input','type':'date'
    }))

    def __init__(self,*arsg,**kwargs):
        super().__init__(*arsg,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control','placeholder':self.fields[field].label})
    date.widget.attrs['min']=timezone.now().date()

# class BookingDetailForm(forms.ModelForm):
#     class Meta:
#         model=BookingCleanerModel
#         fields='__all__'