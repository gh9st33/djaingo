```python
from django.shortcuts import render
from .models import ChatResult, TaskResult

def chat_results(request):
    results = ChatResult.objects.all()
    return render(request, 'app_results/chat_results.html', {'results': results})

def task_results(request):
    results = TaskResult.objects.all()
    return render(request, 'app_results/task_results.html', {'results': results})
```