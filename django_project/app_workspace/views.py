```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Workspace

@login_required
def workspace(request):
    workspace = Workspace.objects.get(user=request.user)
    return render(request, 'app_workspace/workspace.html', {'workspace': workspace})

@login_required
def create_file(request):
    if request.method == 'POST':
        file_name = request.POST.get('file_name')
        workspace = Workspace.objects.get(user=request.user)
        workspace.files.create(name=file_name)
        return redirect('workspace')

@login_required
def edit_file(request, file_id):
    if request.method == 'POST':
        file_content = request.POST.get('file_content')
        workspace = Workspace.objects.get(user=request.user)
        file = workspace.files.get(id=file_id)
        file.content = file_content
        file.save()
        return redirect('workspace')
```