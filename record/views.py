from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'record/index.html', context)

def receive(request):
    context_instance=RequestContext(request)
    print(request.FILES.get('data'))
    return JsonResponse({"msg":"Awesome"})