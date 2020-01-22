from django.urls import path
from reminder.views import add_reminders

app_name = 'reminder'

urlpatterns = [
    path('', add_reminders, name='add_reminders'),
]