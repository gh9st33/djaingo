```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django_project.app_auth.urls')),
    path('chatbot/', include('django_project.app_chatbot.urls')),
    path('workspace/', include('django_project.app_workspace.urls')),
    path('tasks/', include('django_project.app_tasks.urls')),
    path('results/', include('django_project.app_results.urls')),
    path('', include('django_project.app_frontend.urls')),
]
```