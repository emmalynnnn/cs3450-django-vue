from django.http import JsonResponse

def index(request):
    response = JsonResponse({'message': 'Here is some text I got from the backend'})
    response['Access-Control-Allow-Origin'] = '*'
    return response
