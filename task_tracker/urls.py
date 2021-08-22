from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from tasks.urls import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('tasks/', include('tasks.urls')),
]