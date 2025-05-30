import os
import shutil
from configfile import ConfigFilePath

class FileManager:
    def move_files(self):       
        input_files = list(os.scandir(ConfigFilePath.INPUT_DIR))
        if not input_files:
            print("No files to move.")
            return

        for file in input_files:
            if file.is_file():
                print(f"Processing file: {file.name}")
                target = ConfigFilePath.OUTPUT_DIR / file.name
                shutil.move(file.path, str(target))
                print(f"Moved: {file.name}")
               
                
            

        