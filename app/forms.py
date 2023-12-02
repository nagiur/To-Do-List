from django import forms
from .models import TaskModel 

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
        
        labels = {
            'taskTitle': 'Task Title',
            'taskDescription': 'Task Description' 
        }
        widgets = {
            'taskTitle': forms.TextInput(),
            'taskDescription': forms.TextInput(),
        }