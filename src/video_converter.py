import os
import subprocess
import ffmpeg

def video_converter(path):
    filename, extension = os.path.splitext(path)
    if extension != ".mp4" and extension != ".jpg" and extension != ".png":
        mp4_path = filename + ".mp4"
        file = ffmpeg.input(path)
        v1 = file.video
        a1 = file.audio
        out = ffmpeg.output(v1, a1, mp4_path)
        out.run()
    else:
        mp4_path = path
        
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', mp4_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    time = float(result.stdout)
    
    return mp4_path, int(time)