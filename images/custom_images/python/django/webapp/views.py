from django.http import JsonResponse
from webapp import settings

def home(request):
    context = dict()
    context['message'] = "It works fine"
    context['database_name'] = settings.DJANGO_DB
    context['database_user'] = settings.DJANGO_USER
    return JsonResponse(context)