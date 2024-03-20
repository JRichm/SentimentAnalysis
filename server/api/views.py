import json
from django.http import JsonResponse
from django.middleware.csrf import get_token

def EndpointView(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            json_data = json.loads(request.body)
            data = {'message': 'request received', 'data': json_data}
            print(data)
            return JsonResponse(data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Handle other request methods if needed
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
        

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})