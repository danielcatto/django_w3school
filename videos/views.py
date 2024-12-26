import os
from utils.lista_arquivos.main import lista_videos
from utils.converte_videos import ffmpeg
from django.http import HttpResponse
from django.template import loader

from moviepy import VideoFileClip, TextClip, CompositeVideoClip

def index(request):    
    vi = lista_videos('midia_videos')
    
    print(f'teste vi {vi}')
    # Fetches all members from the database
    template = loader.get_template('index.html')
    
    context = {
        'vi': vi    }
    return HttpResponse(template.render(context, request))    


def exibir_video(request, nome):
    clip = VideoFileClip(f'static/videos/{nome}.mp4')
    duracao_em_segundos = clip.duration
    
    template = loader.get_template('exibir_video.html')
    context= {
        'nome':nome,
    }
    return HttpResponse(template.render(context))

def videos_novos(request):    
    
    vi = lista_videos('upload_videos_novos')
    if len(vi) > 0:
        #mnffmpeg.conversao()
        print(f'teste vi {vi}')
    else:
        print('não há videos novos por enquanto :D')
    # Fetches all members from the database
    template = loader.get_template('videos_novos.html')
    
    context = {
        'vi': vi    }
    return HttpResponse(template.render(context, request))    
