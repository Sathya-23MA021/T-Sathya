from .models import render, redirect
from .models import *
 # Create a form for MoodTracker

def mood_tracker_list(request):
    if request.method =='POST':
        name =request.POST.get('name')
        date =request.POST.get('date')
        time =request.POST.get('time')    
        mood =request.POST.get('mood')
        mood_intensity =request.POST.get('mood_intensity')
        performance =request.POST.get('performance')
        stress_level =request.POST.get('stress_level')
        energy_level =request.POST.get('energy_level')
        physical_health =request.POST.get('physical_health')
        activities =request.POST.get('activities')
        social_interaction =request.POST.get('social interaction')
        weather =request.POST.get('weather')
        mental_clarity =request.POST.get('mental_clarity')
        gratitude_notes =request.POST.get('gratitude_notes')
        self_care =request.POST.get('self_care')
        return redirect('mood_tracker_list')
    entries=MoodTracker.objects.all()
    return render(request,'index.html',{'entries':entries})    