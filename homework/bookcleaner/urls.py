from django.conf.urls import url
from django.urls import path
from .views import BookCleanerView,BookOrderView,BookingListView,CleanerListView

app_name='bookcleaner'

urlpatterns=[
    url(r'^book/$',BookCleanerView.as_view(),name='book'),
    url(r'^bookingorder/$',BookOrderView.as_view(),name='bookingorder'),
    path('bookingdetail/',BookingListView.as_view(),name='bookinglist'),
    path('cleanerlist/',CleanerListView.as_view(),name='cleanerlist'),
]