from django.shortcuts import render
from .models import Blog
from django.utils.translation import gettext as _

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from django.conf import settings
import logging

from elasticsearch_dsl.query import MultiMatch
from .documents import Blogdocument
# Create your views here.

def main(request):
    
    return render(request, 'main.html', {'blogs' : Blog.objects.all()})


def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        query = MultiMatch(query=q, fields=["title", "content"], fuzziness="AUTO")

        s = Blogdocument.search().query(query)[0:5]
        context["blogs"] = s
    return render(request, "chat.html", context)



# logger = logging.getLogger(__name__)
# openai.api_key = settings.OPENAI_API_KEY


# @csrf_exempt
# def chat(request):
#     if request.method == 'POST':
#         try:
#             user_message = request.POST.get('message', '')
#             if not user_message:
#                 logger.error('No message received from user.')
#                 return JsonResponse({'message': 'No message received'}, status=400)
            
#             logger.debug(f'Received message from user: {user_message}')
            
#             response = openai.Completion.create(
#                 model="gpt-3.5-turbo",
#                 prompt=user_message,
#                 max_tokens=150
#             )
#             gpt_message = response.choices[0].text.strip()
            
#             logger.debug(f'GPT-3 response: {gpt_message}')
            
#             return JsonResponse({'message': gpt_message})
        
#         except Exception as e:
#             logger.error(f'Error occurred: {e}')
#             return JsonResponse({'message': 'An error occurred'}, status=500)
    
#     return render(request, 'chat.html')


