import json
from django.http import JsonResponse

def EndpointView(request):
    if request.method == 'GET':
        # Handle GET request
        data = {'message': 'This is a GET request', 'data': request.GET.dict()}
        return JsonResponse(data)
    elif request.method == 'POST':
        # Handle POST request
        data = {'message': 'This is a POST request', 'data': request.POST.dict()}
        return JsonResponse(data)
    else:
        # Handle other request methods
        return JsonResponse({'error': 'Method not allowed'}, status=405)