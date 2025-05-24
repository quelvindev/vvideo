import logging
from pathlib import Path
from machine.source_folder import SourceFolder

class LogConfig:
    def __init__(self, filename='vvideo.log', filemode='a', level=logging.DEBUG,dir_log = None):
        default_log_dir =  Path(Path.home().anchor)/'vvideo_log' if dir_log is None else Path(dir_log)
        default_log_dir.mkdir(parents=True,exist_ok=True)
        folder = default_log_dir/filename

        self.logger = logging.getLogger(str(folder))
        self.logger.setLevel(level)

        # Evita adicionar múltiplos handlers se o logger já tiver
        if not self.logger.handlers:
            handler = logging.FileHandler(folder, mode=filemode)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
