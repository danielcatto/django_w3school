import os  # Interação com o sistema operacional
import fnmatch  # Padrões de correspondência de strings
import sys  # Acesso a variáveis e funções específicas do sistema


def conversao():
    # Define o comando FFmpeg com base na plataforma
    comando_ffmpeg = 'ffmpeg' if sys.platform == 'linux' else 'ffmpeg.exe'

    # Parâmetros de conversão FFmpeg
    codec_video =  '-c:v libx264'  # Codificador de vídeo H.264
    crf = '-crf 23'  # Qualidade constante
    preset = '-preset ultrafast'  # Preset de alta velocidade
    codec_audio =  '-c:a aac'  # Codificador de áudio AAC
    bitrate_audio = '-b:a 320k'  # Taxa de bits de áudio
    #debug = ''
    debug = '-ss 00:01:00 -to 00:01:10'  # Processa apenas os primeiros 10 segundos
    nova_extensao = '.mp4'

    # Caminhos dos diretórios
    caminho_origem = '/home/daniel-catto/projeto/django_w3school/static/upload_videos_novos'  # Diretório de origem dos vídeos
    caminho_destino = '/home/daniel-catto/projeto/django_w3school/static/videos'  # Diretório de destino dos vídeos convertidos

    # Percorre todos os arquivos MKV no diretório de origem e seus subdiretórios
    for raiz, pasta, arquivos in os.walk(caminho_origem):
        for arquivo in arquivos:
            if fnmatch.fnmatch(arquivo, '*.mkv'):  # Filtra arquivos MKV
                print(arquivo)
                caminho_completo = os.path.join(raiz, arquivo)  # Caminho completo do arquivo
                nome_arquivo, extensao_arquivo  = os.path.splitext(caminho_completo)  # Separa nome e extensão
                caminho_legenda = arquivo + '.str'

                if os.path.isfile(caminho_legenda):
                    input_legenda = f'-i "{caminho_legenda}"'
                    map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
                else:
                    input_legenda = ''
                    map_legenda = ''

                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

                arquivo_saida = f'{caminho_destino}/{nome_arquivo}{nova_extensao}'

                comando =  f'{comando_ffmpeg} -hide_banner -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {debug} "{arquivo_saida}"'
                os.system(comando)