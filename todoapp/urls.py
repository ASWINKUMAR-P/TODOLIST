from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addTask, name='add'),
    path('complete/<int:id>', views.completeTask, name='complete'),
    path('delete/<int:id>', views.deleteTask, name='delete'),
]