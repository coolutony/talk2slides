from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
import base64


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'record/index.html', context)

def receive(request):
    context_instance=RequestContext(request)
    print(request.FILES.get('data'))
    data = request.FILES.get('data') #This data is blob
    return JsonResponse({"msg":"Awesome"}) #TODO: appropriate response