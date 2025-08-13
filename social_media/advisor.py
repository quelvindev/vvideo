from social_media.youtube import DownYouTube
from social_media.tiktok import DownTiktok
from social_media.instagram import DownInstagram
from social_media.x import DownX

import tldextract

class Advisor:

    def __init__(self):
        ...
        self.video = None
        
    def lighthouse(self,url):
        print(f'chegou no Advisor {url.upper()}')
        ext_domain = tldextract.extract(url.upper())

        
        if ext_domain.domain == 'YOUTUBE':
            self.video = DownYouTube()
            self.video.download(url)
            
        elif ext_domain.domain == 'TIKTOK':
            self.video =DownTiktok()
            self.video.download(url)

        elif ext_domain.domain == 'INSTAGRAM':
            self.video =DownInstagram()
            self.video.download(url)

        elif ext_domain.domain == 'X':
            print(f'download x {url}')
            self.video =DownX()
            self.video.download(url)

        # if str(url.upper()).__contains__('YOUTUBE'):
        #     self.video = DownYouTube()
        #     self.video.download(url)
        
            
        
    