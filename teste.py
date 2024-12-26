from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from mutagen.mp4 import MP4



clip = VideoFileClip('static/videos/caninos_brancos-acao_aventura.mp4')
duracao_em_segundos = clip.duration 

minutos = duracao_em_segundos // 60
segundos = duracao_em_segundos % 60
print(f'{minutos}:{segundos}')


video = MP4('static/videos/caninos_brancos-acao_aventura.mp4')
titulo = video.tags['title'][0]
