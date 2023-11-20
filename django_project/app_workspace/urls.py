```python
from django.urls import path
from . import views

app_name = 'app_workspace'

urlpatterns = [
    path('', views.workspace_view, name='workspace'),
    path('create_file/', views.create_file, name='create_file'),
    path('edit_file/<str:filename>/', views.edit_file, name='edit_file'),
    path('delete_file/<str:filename>/', views.delete_file, name='delete_file'),
]
```