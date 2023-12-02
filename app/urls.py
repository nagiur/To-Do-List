from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_tasks, name='show_tasks'), # Home URL
    path('show_tasks', views.show_tasks, name='show_tasks'),
    path('complete_tasks', views.complete_tasks, name="complete_tasks"),
    
    path('add_task', views.add_task, name="add_task"),
    path('delete/<int:task_id>', views.delete_task, name="delete_task"),
    path('edit/<int:task_id>', views.edit_task, name="edit_task"),
    path('make_complete/<int:task_id>', views.make_complete_task, name="make_complete_task"),

    
]
