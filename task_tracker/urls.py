from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from tasks.urls import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', include('tasks.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
