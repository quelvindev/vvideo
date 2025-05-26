
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pytubefix import YouTube
from machine.log_config import LogConfig
from machine.source_folder import SourceFolder


class DownYouTube:

    def __init__(self):
        self.folder = SourceFolder()
        self.log = LogConfig()
        

    def dowload(self,source ):
        self.log.info('Coletando url')
        yt = YouTube(source)

        print(yt.title)

        ys = yt.streams.get_highest_resolution()
        folder = self.folder.create_folder_vid()
        ys.download(folder)


if __name__ == "__main__":
    down = DownYouTube()
    down.dowload('https://www.youtube.com/watch?v=u9feBros-2k')