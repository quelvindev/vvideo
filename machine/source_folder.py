from pathlib import Path

class SourceFolder:
    def __init__(self):
        self.home = Path.home()
        self.source = Path(self.home.anchor)
        self.whats_names = ["Desktop", "Área de Trabalho"]
        self.my_folder_vid = 'vvideo'
        self.my_folder_log = 'vvideo_log'
        self.dir_vid = None
        self.dir_log = None

    
    def mk_folders(self):
        self.create_folder_vid()
        self.create_folder_log()

    def create_folder_vid(self):
 
        for name in self.whats_names:
            dir_path = self.home / name
            if dir_path.exists():
                folder = dir_path / self.my_folder_vid
                folder.mkdir(exist_ok=True)
                self.dir_vid = folder
                return self.dir_vid

    def create_folder_log(self):

        folder = self.source /self.my_folder_log
        folder.mkdir(exist_ok=True)
        self.dir_log = folder
        return self.dir_log
        



if __name__ == '__main__':
    
    folders = SourceFolder()
    folders.mk_folders()