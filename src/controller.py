from file_formater import file_formater
from user_input import user_input
from video_converter import video_converter
from recognizer import recognizer

def controller():
    code, path = user_input()
    print("\nAll input given. Checking for video conversion.\n")
    path, length_of_vid = video_converter(path)
    print("\nAll video converted. Running the recognizer. Please be patient.\n")
    result_list = recognizer(code, path, length_of_vid)
    print("\nRecognizer run. Converting to specified file format.\n")
    file_formater(result_list)
    print("\nFile saved as X in Y.\n")
    
if __name__ == '__main__':
    controller()