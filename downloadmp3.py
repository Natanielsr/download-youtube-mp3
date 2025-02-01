import yt_dlp

def download_and_convert_to_mp3(url, cookies_file=r"cookies.txt" , output_path='musics/%(title)s.%(ext)s'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # Extrai o áudio
        'audioformat': 'mp3',  # Converte para mp3
        'outtmpl': output_path,  # Caminho de saída do arquivo
        'cookies': cookies_file,  # Usando os cookies exportados
        'postprocessors': [{  # Usando ffmpeg para conversão
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Qualidade do áudio
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Exemplo de uso
url = 'https://www.youtube.com/watch?v=_coxY0UDijA'
download_and_convert_to_mp3(url)
