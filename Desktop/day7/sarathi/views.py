from django.shortcuts import render,redirect
from .models import *
from accounts.forms import RegistrationForm
# Create your views here.
def homepage(request):
    return render (request,'index.html')




def student_form(request):
    if request.method =='POST':
        name =request.POST.get('name')
        roll_no=request.POST.get('roll_no')
        email=request.POST.get('email')
        student.object.create(name=name,roll_no=roll_no,email=email)
        return redirect('student_form')
    students=student.object.all()   
    return render(request,'index.html',{'students':students})




def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:        
        form = RegistrationForm()
    return render(request,'registration/signup.html',{'form':form})    