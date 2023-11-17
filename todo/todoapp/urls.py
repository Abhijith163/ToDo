
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('tdlete/<int:id>/', views.tdelete, name='tdelete'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    
    
]