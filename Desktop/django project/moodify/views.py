# from django.shortcuts import get_object_or_404, render, redirect
# from .models import *
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages




           
           
# def mood_tracker_list(request):
#     if request.method =='POST':
#         username= request.POST.get('username') # Fetch the User instance
#         date = request.POST.get('date')
#         time = request.POST.get('time')    
#         mood = request.POST.get('mood')
#         mood_intensity = request.POST.get('mood_intensity')
#         performance = request.POST.get('performance')
#         stress_level = request.POST.get('stress_level')
#         energy_level = request.POST.get('energy_level')
#         physical_health = request.POST.get('physical_health')
#         activities = request.POST.get('activities')
#         social_interaction = request.POST.get('social_interaction')  # Fixed key
#         weather = request.POST.get('weather')
#         mental_clarity = request.POST.get('mental_clarity')
#         gratitude_notes = request.POST.get('gratitude_notes')
#         self_care = request.POST.get('self_care')

#         MoodTracker.objects.create(
#             username=username, date=date, time=time, mood=mood,
#             mood_intensity=mood_intensity, performance=performance, stress_level=stress_level,
#             energy_level=energy_level, physical_health=physical_health, activities=activities,
#             social_interaction=social_interaction, weather=weather, mental_clarity=mental_clarity,
#             gratitude_notes=gratitude_notes, self_care=self_care
#         )

#         return redirect('mood_tracker_list')

#     entries = MoodTracker.objects.all()
#     return render(request, 'index.html', {'entries': entries})


    


    
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#             return redirect('signup')

#         user = User.objects.create_user(username=username, email=email, password=password)
#         messages.success(request, "Account created successfully.")
#         return redirect('login')

#     return render(request, 'signup.html')



      
 
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('mood_tracker_list')
#         else:
#             messages.error(request, "Invalid credentials.")
#             return redirect('login')

#     return render(request, 'login.html')  

# def logout_view(request):
#     logout(request)
#     return redirect('login') 


    
# def edit_MoodTracker(request, pk):
#     entries = get_object_or_404(MoodTracker, pk=pk)

#     if request.method == "POST":
#         entries.title = request.POST.get("title")
#         entries.description = request.POST.get("description")
#         entries.credits = request.POST.get("credits")
#         entries.save()
#         return redirect("mood_tracker_list")

#     return render(request, "edit.html", {
#         "edit_course": entries,
#         "entries": MoodTracker.objects.all()
#     })


# def delete_MoodTracker(request, pk):
#     entries = get_object_or_404(MoodTracker, pk=pk)
#     entries.delete()
#     return redirect("mood_tracker_list")
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import MoodTracker

def mood_tracker_list(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        date = request.POST.get('date')
        time = request.POST.get('time')
        mood = request.POST.get('mood')
        mood_intensity = request.POST.get('mood_intensity')
        performance = request.POST.get('performance')
        stress_level = request.POST.get('stress_level')
        energy_level = request.POST.get('energy_level')
        physical_health = request.POST.get('physical_health')
        activities = request.POST.get('activities')
        social_interaction = request.POST.get('social_interaction')
        weather = request.POST.get('weather')
        mental_clarity = request.POST.get('mental_clarity')
        gratitude_notes = request.POST.get('gratitude_notes')
        self_care = request.POST.get('self_care')

        MoodTracker.objects.create(
            username=username, date=date, time=time, mood=mood,
            mood_intensity=mood_intensity, performance=performance, stress_level=stress_level,
            energy_level=energy_level, physical_health=physical_health, activities=activities,
            social_interaction=social_interaction, weather=weather, mental_clarity=mental_clarity,
            gratitude_notes=gratitude_notes, self_care=self_care
        )

        return redirect('mood_tracker_list')

    entries = MoodTracker.objects.all()
    return render(request, 'index.html', {'entries': entries})

def edit_MoodTracker(request, pk):
    entries = get_object_or_404(MoodTracker, pk=pk)

    if request.method == "POST":
        entries.mood = request.POST.get("mood")
        entries.mood_intensity = request.POST.get("mood_intensity")
        entries.performance = request.POST.get("performance")
        entries.stress_level = request.POST.get("stress_level")
        entries.energy_level = request.POST.get("energy_level")
        entries.physical_health = request.POST.get("physical_health")
        entries.activities = request.POST.get("activities")
        entries.social_interaction = request.POST.get("social_interaction")
        entries.weather = request.POST.get("weather")
        entries.mental_clarity = request.POST.get("mental_clarity")
        entries.gratitude_notes = request.POST.get("gratitude_notes")
        entries.self_care = request.POST.get("self_care")
        entries.save()

        return redirect("mood_tracker_list")

    return render(request, "edit.html", {"entries": entries})

def delete_MoodTracker(request, pk):
    entries = get_object_or_404(MoodTracker, pk=pk)
    entries.delete()
    return redirect("mood_tracker_list")

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
            return redirect('mood_tracker_list')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
