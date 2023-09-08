```python
from django.http import JsonResponse
from django.views import View
from .tasks import process_codex_task
from app_workspace.models import Workspace
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class TaskView(View):
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        workspace_id = request.POST.get('workspace_id')
        code = request.POST.get('code')

        workspace = Workspace.objects.get(id=workspace_id)

        if workspace.user != request.user:
            return JsonResponse({'error': 'Not authorized'}, status=401)

        task = process_codex_task.delay(code)

        return JsonResponse({'task_id': task.id}, status=202)

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        task_id = request.GET.get('task_id')

        task = process_codex_task.AsyncResult(task_id)

        if task.state == 'PENDING':
            response = {
                'state': task.state,
                'status': 'Task is currently being processed'
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'result': task.result,
            }
        else:
            response = {
                'state': task.state,
                'status': str(task.info),
            }

        return JsonResponse(response)
```