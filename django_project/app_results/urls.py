```python
from django.urls import path
from . import views

app_name = 'app_results'

urlpatterns = [
    path('results/', views.ResultView.as_view(), name='results'),
]
```