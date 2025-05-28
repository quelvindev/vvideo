from social_media.youtube import DownYouTube
class Advisor:

    def __init__(self):
        ...
        self.youtube = DownYouTube()
    def lighthouse(self,url):
        print(f'chegou no Advisor {url.upper()}')
        if str(url.upper()).__contains__('YOUTUBE'):
            self.youtube.dowload(url)