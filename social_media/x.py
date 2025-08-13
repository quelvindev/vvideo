import yt_dlp
from machine.log_config import LogConfig
from machine.source_folder import SourceFolder

class DownX:

    def __init__(self):
        self.folder = SourceFolder()
        self.log = LogConfig()

    def download(self,source): 
        folder = self.folder.create_folder_vid()
        ydl_opts = {
            "outtmpl":f"{folder}/%(title)s.%(ext)s",  
            }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([source])