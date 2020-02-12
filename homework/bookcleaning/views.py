from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,TemplateResponseMixin,ContextMixin
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.views.generic import View
from django.contrib.auth import authenticate
from .forms import RegistrationForm,LoginForm
from django.contrib.messages.views import messages
from .forms import CleanerForm
from .models import User
from django.views.generic.detail import DetailView

# Create your views here.
class BookCleaningView(TemplateView):
    template_name="home.html"
 
    def get_context_data(self, **kwargs):
        context = super(BookCleaningView,self).get_context_data(**kwargs)
        return context

class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'signup.html',{'form':form})

    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"You Are Register Successfully Now Login !")
        return render(request,'signup.html',{'form':form})

class LoginView(View):
    def get(self,request):
        lform=LoginForm()
        return  render(request,'login.html',{'form':lform})

    def post(self,request):
        form1=LoginForm(data=request.POST)
        if form1.is_valid():
            contact=form1.cleaned_data.get('contact')
            password=form1.cleaned_data.get('password')
            user=authenticate(contact=contact,password=password)
            if user is not None: 
                login(request,user)
                # print(request.user)
                return redirect ('bookcleaning:profile',pk=user.id)
            else:
                messages.error(request,'User Not Found please Enter Valid data'+str(form1.errors))
        return render(request,'login.html',{'form':form1})

class ProfileView(DetailView):
    model=User
    template_name="profile.html"
    extra_context={'form':CleanerForm()}

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('bookcleaning:home')

class CleanerCreate(View):

    def get(self,request):
        # try:
        #     profile = request.user
        # except User.DoesNotExist:
        #     profile = User(user=request.user)

        form=CleanerForm()
        return render(request,'cleancreate.html',{'form':form})
    
    def post(self,request):
        # try:
        #     profile = request.user
        # except User.DoesNotExist:
        #     profile = User(user=request.user)
            
        form=CleanerForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            request.user.is_cleaner=True
            request.user.save()
            obj.save()
            return redirect("bookcleaning:profile",pk=request.user.pk)
