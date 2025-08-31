import os
import sys
import platform
import subprocess

class Utis:

    def __init__(self):
        ...
    
    def ensure_package_installed(self,package_name):


        result = subprocess.run(
        ["pip", "show", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
        )
        print(f'returncode{result.returncode}')
        print(f'stdout{result.stdout}')
        if result.returncode ==1:
           subprocess.run(
            ["pip", "install", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
             )

    #ensure_package_installed("tiktok_downloader")