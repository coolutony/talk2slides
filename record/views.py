from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
from record import naver_api_utils as naive
import configparser
import os
config = configparser.ConfigParser()
print(os.getcwd())
config.read('record/config.ini')

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'record/index.html', context)

def receive(request):
    context_instance=RequestContext(request)
    print(request.FILES.get('data'))
    data = request.FILES.get('data').read() #This data is blob
    text = naive.parse_audio(config['NAVER_AI_API']['client_id'],\
                      config['NAVER_AI_API']['client_secret'],\
                      audio_bytes=data, lang="Kor")
    print(text)
    return JsonResponse({"msg":text})