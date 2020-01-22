from django.urls import path
from reminder.views import reminders_list

app_name = 'reminder'

urlpatterns = [
    path('', reminders_list, name='reminders_list'),
]