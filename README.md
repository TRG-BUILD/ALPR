# ALPR for students
This is a simplified program that takes in video and outputs what numberplates are present in the video in a specified file format. The program needs a small amount of setup.

## How to use
First install docker (https://docs.docker.com/engine/install/) and git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

To verify they are already on your system or installed correctly, give these commands to the terminal:
- `git --version`
- `docker run hello-world`

After this installtion proces, go into the directory you want to have this program installed, using the terminal window:

`cd /path/to/your/destination`

Git clone the repository:
- `git clone https://github.com/TRG-BUILD/ALPR.git`

Then build the application so it can be used.
- `docker build --tag alpr .`
(The `.` at the end is important!)

Then run the container in interactive mode (-it) and follow the instructions.
- `docker run -it alpr`

### Supported ALPR algorithms
Presently, only openalpr is a supported machine learning model. Will be expanded upon.

### Supported file formats
Presently, only .csv is a supported format. Will be expanded upon.

## How is the program set up?
The program primarily functions through its `Dockerfile`. The `Dockerfile` creates a seperate, small linux installation on the machine running the docker commands. This linux operative system then gets just the things installed which are necessary to make the different machine learning models and python scripts work. This makes it possible to skip all the unnecessary installation process of the different machine learning models and dependencies, as well make this program possible to run on any computer, since it basically is its own linux distribution.

The program has a `/src` folder which contains the controller, the user_input, the recognizer, the file_formater and the video_converter.

The controller calls the user_input, the video_converter, the recognizer and the file_formatter in this order.

The user_input takes all relevant user_input from the user. Where to find the video, what file format is wanted, etc.

The video_converter checks if the chosen video (or set of videos) is in a correct format. If not, it will create a new video file based on the given video to an understandable format.

The recognizer uses the chosen ALPR/ANPR machine learning algorithm, which have been installed. The Dockerfile installs different models which can be selected by the user.

The file_formater takes the list of recognized numberplates and turns it into the chosen file format, also making sure the data is presented as the user wants it.

## Want to know more
The basis for this program is primarily based on the following article:

https://www.pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/