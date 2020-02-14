from django.shortcuts import render
from django.http import JsonResponse
from django.template import RequestContext
from record import naver_api_utils as naive
import configparser
import os
config = configparser.ConfigParser()
config.read('record/config.ini')


def index(request, current_template="title_template"):
    template_filenames = [
        "title_template",
        "paragraph_template",
        "image_template",
        "maps_template",
        "list_template",
    ]
    if current_template == None:
        current_template = template_filenames[0]
    print(current_template)
    context = {"template_filenames":template_filenames,
               "current_template":current_template}
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