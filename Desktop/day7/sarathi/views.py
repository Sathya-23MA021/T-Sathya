from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render (request,'index.html')

    


def student_form(request):
    if request.method =='POST':
        name =request.POST.get('name')
        roll_no=request.POST.get('roll_no')
        email=request.POST.get('email')
        student.objects.create(name=name,roll_no=roll_no,email=email)
        return redirect('student_form')
    students=student.objects.all()   
    return render(request,'index.html',{'students':students})



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Account created successfully.")
        return redirect('login')

    return render(request, 'signup.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_form')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')  

def logout_view(request):
    logout(request)
    return redirect('login') 



def student_biodata(request):
    if request.method == 'POST':
        dept = request.POST.get('dept')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile_no = request.POST.get('mobile_no')
        stream = request.POST.get('stream')
        biodata.objects.create(dept=dept, age=age, gender=gender, mobile_no=mobile_no, stream=stream)
        return redirect('student_biodata')
    biodatas = biodata.objects.all()
    return render(request,'biodata.html', {'biodatas': biodatas})    




def edit_biodata(request, pk):
    biodatas = get_object_or_404(biodata, pk=pk)

    if request.method == "POST":
        biodatas.dept = request.POST.get("dept")
        biodatas.age = request.POST.get("age")
        biodatas.gender  = request.POST.get("gender")
        biodatas.mobile_no = request.POST.get("mobile_no")
        biodatas.stream = request.POST.get("stream")
        biodatas.save()
        return redirect("edit_biodata")

    return render(request, "edit.html", {
        "edit_biodata": biodatas,
        "biodatas": biodata.objects.all()
    })


def delete_biodata(request, pk):
    biodatas = get_object_or_404(biodata, pk=pk)
    biodatas.delete()
    return redirect("delete_biodata")
