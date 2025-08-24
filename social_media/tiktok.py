import os
import tiktok_downloader
from machine.log_config import LogConfig
from machine.source_folder import SourceFolder

class DownTiktok:
    def  __init__(self):
        self.folder = SourceFolder()
        self.log = LogConfig()
    

    def download(self,source):
        link_tiktok = source
        if link_tiktok:
            folder = self.folder.create_folder_vid()
            os.system(f'python -m tiktok_downloader --snaptik --url {link_tiktok} --save {folder}/tiktok_video.mp4')
            
        else:
            print('link inválido')



if __name__ == '__main__':
    tiktok = DownTiktok()
    tiktok.download('https://www.tiktok.com/@girodenoticias55/video/7508852477710601478')