from django.http import JsonResponse

def home(request):
    context = dict()
    context['message'] = "It works fine"
    return JsonResponse(context)