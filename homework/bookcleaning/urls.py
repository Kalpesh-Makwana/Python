from django.conf.urls import url
from django.urls import path
from .views import BookCleaningView,RegistrationView,LoginView,LogoutView,ProfileView,CleanerCreate

app_name='bookcleaning'

urlpatterns=[
    url(r'^$',BookCleaningView.as_view(),name='home'),
    url(r'^signup/$',RegistrationView.as_view(),name='signup'),
    url(r'^login/$',LoginView.as_view(),name='login'),
    url(r'^logout/$',LogoutView.as_view(),name='logout'),
    path('profile/<int:pk>',ProfileView.as_view(),name='profile'),
    # url(r'^profile/(?P<pk>[0-9]+)/$',ProfileView.as_view(),name='profile'),
    url(r'^cleancreate/$',CleanerCreate.as_view(),name='cleancreate'),

]

