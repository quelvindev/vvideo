import instaloader
from machine.log_config import LogConfig
from machine.source_folder import SourceFolder


class DownInstagram:
    def __init__(self):
        self.folder = SourceFolder()
        self.log = LogConfig()

    def download(self,source): 
        insta = instaloader.Instaloader(   
                    download_pictures=False,
                    download_video_thumbnails=False,
                    download_videos=True,
                    save_metadata=False,
                    download_comments = False, 
                    post_metadata_txt_pattern = "" )
        shortcode = source.split("/")[-2]
        post = instaloader.Post.from_shortcode(insta.context, shortcode)
        #description =  (post.caption[:20] if post.caption else "")
        #user = post.owner_username
        folder = self.folder.create_folder_vid()
        insta.download_post(post, target=folder)



