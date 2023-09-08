```python
from django.utils.deprecation import MiddlewareMixin
from elasticsearch import Elasticsearch
import json

class LoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.es = Elasticsearch()

    def process_request(self, request):
        request._logging_start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, '_logging_start_time'):
            execution_time = time.time() - request._logging_start_time
            log_data = {
                'user': str(request.user),
                'path': request.path,
                'method': request.method,
                'execution_time': execution_time,
                'status_code': response.status_code
            }
            self.es.index(index='django_logs', body=json.dumps(log_data))
        return response
```