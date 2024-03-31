
# Create your views here.
from django.http import HttpResponse

def set_cookie(______):
    response = HttpResponse("Cookie set!")
    response.set_cookie('username', 'lalitha')

    return response

def get_cookie(request):
    username = request.COOKIES.get('username','Guest')
    return HttpResponse(f"Hello, {username}!")