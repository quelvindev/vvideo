from social_media.youtube import DownYouTube
from social_media.tiktok import DownTiktok
class Advisor:

    def __init__(self):
        ...
        self.video = None
        
    def lighthouse(self,url):
        print(f'chegou no Advisor {url.upper()}')
        if str(url.upper()).__contains__('YOUTUBE'):
            self.video = DownYouTube()
            self.video.download(url)
            
        elif str(url.upper()).__contains__('TIKTOK'):
            self.video =DownTiktok()
            self.video.download(url)
            
        
    