```python
from django.urls import path
from . import views

app_name = 'app_tasks'

urlpatterns = [
    path('start_task/', views.start_task, name='start_task'),
    path('get_task_status/<str:task_id>/', views.get_task_status, name='get_task_status'),
]
```