from django.http import JsonResponse
from webapp import settings

def home(request):
    context = dict()
    context['message'] = "It works fine"
    context['database'] = settings.DJANGO_DB
    return JsonResponse(context)