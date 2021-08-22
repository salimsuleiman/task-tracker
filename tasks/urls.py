from django.urls import path
from .views import *


urlpatterns = [
    path('', get_all_tasks),
    path('<int:pk>', get_task),
    path('update/<int:pk>/', update_task),
    path('create/', create_task),
    path('delete/<int:taskID>/', delete_task)
]