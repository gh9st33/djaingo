```python
from django.http import JsonResponse
from django.views import View
from openai import OpenAI, ChatCompletion
from django_project.settings import OPENAI_API_KEY

openai = OpenAI(OPENAI_API_KEY)

class ChatBotView(View):
    def post(self, request, *args, **kwargs):
        message = request.POST.get('message')
        chat = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        response = chat['choices'][0]['message']['content']
        return JsonResponse({'response': response})
```