from django.urls import path
from reminder.views import reminders_list, add_Reminders

app_name = 'reminder'

urlpatterns = [
    path('', reminders_list, name='reminders_list'),
    path('/toadd/', add_Reminders, name='add_Reminders')
]