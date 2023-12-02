from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=20) 
    taskDescription = models.CharField(max_length=30)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.taskTitle
    
    