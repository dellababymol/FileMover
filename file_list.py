import os
from configfile import ConfigFilePath

class FileList:
    
    def list_files(self):
       
        entries = os.scandir(ConfigFilePath.INPUT_DIR)

        for entry in entries:
            if os.path.isfile(entry):
                print('File:',entry.name)
                
            elif os.path.isdir(entry):
                print('Directory:',entry.name)

        