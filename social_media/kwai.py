import requests
from bs4 import BeautifulSoup
from machine.log_config import LogConfig
from machine.source_folder import SourceFolder

class DownKwai:

    def __init__(self):
        self.folder = SourceFolder()
        self.log = LogConfig()

    def download(self,url):
        headers = {
        "User-Agent": "Mozilla/5.0"
        }

    
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print("Erro ao acessar página:", resp.status_code)
            return
        soup = BeautifulSoup(resp.text, "html.parser")

    
        meta_video = soup.find("meta", property="og:video")
        if not meta_video:
            print("Não foi possível encontrar o vídeo no HTML.")
            return

        video_url = meta_video["content"]
        print("URL do vídeo:", video_url)

    
        video_resp = requests.get(video_url, headers=headers, stream=True)
        with open('kwai_video.mp4', "wb") as f:
            for chunk in video_resp.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Download concluído:")



