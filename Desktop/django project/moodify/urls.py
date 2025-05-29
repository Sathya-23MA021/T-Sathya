from django.urls import path 
from . views import *

urlpatterns = [
    path('mood_tracker_list/',mood_tracker_list, name='mood_tracker_list'),
    path('signup_view/',signup_view, name='signup'),
    path('login_view/',login_view, name='login'),
     path('edit_MoodTracker/<int:pk>/',edit_MoodTracker, name='edit_MoodTracker'),
    path('delete_MoodTracker/<int:pk>/',delete_MoodTracker, name='delete_MoodTracker'),
]