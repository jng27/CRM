from django.db import models 

class toDoList(models.Model):
    content = models.TextField()
    