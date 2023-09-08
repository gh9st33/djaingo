```python
from django.db import models
from django.contrib.auth.models import User

class Workspace(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
```