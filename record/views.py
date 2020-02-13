from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
import base64
import naver_api_utils as naive
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {}
    return render(request, 'record/index.html', context)

def receive(request):
    context_instance=RequestContext(request)
    print(request.FILES.get('data'))
    data = request.FILES.get('data') #This data is blob
    text = naive.parse_audio(config['NAVER_AI_API']['client_id'],\
                      config['NAVER_AI_API']['client_secret'],\
                      audio_bytes=data, lang="Kor")
    return JsonResponse({"msg":text}) #TODO: appropriate response