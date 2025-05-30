from file_manager import FileManager
from file_list import FileList
from configfile import ConfigFilePath

def main():
    print("Input Dir:", ConfigFilePath.INPUT_DIR)
    print("Output Dir:", ConfigFilePath.OUTPUT_DIR)
    list =  FileList()
    list.list_files()
    manager = FileManager()
    manager.move_files()

if __name__ == "__main__":
    main()
# This is the main entry point of the application.