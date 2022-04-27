# ALPR for students
This is a simplified program that takes in video and outputs what numberplates are present in the video in a specified file format. The program needs a small amount of setup.

## How to use
Git clone the repository into a chosen folder, then run:
- `python main.py`

Then follow the instructions.

### Supported ALPR algorithms
Presently, only openalpr is a supported machine learning model. Will be expanded upon.

### Supported file formats
Presently, only .csv is a supported format. Will be expanded upon.

## How is the program set up?
The program has a `/src` folder which contains the controller, the user_input, the recognizer, the file_formater and the video_converter.

The controller calls the user_input, the video_converter, the recognizer and the file_formatter in this order.

The user_input takes all relevant user_input from the user. Where to find the video, what file format is wanted, etc.

The video_converter checks if the chosen video is in a correct format. If not, it will create a new video file based on the given video to an understandable format.

The recognizer uses the chosen ALPR/ANPR machine learning algorithm, which have been installed. How to install 

## Want to know more
The basis for this program is primarily based on the following article:

https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/