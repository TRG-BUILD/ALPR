import os
import subprocess
import ffmpeg

def video_loader(videos_dir_path):
    file_list = os.listdir(videos_dir_path)
    
    video_list = []
    for file_name in file_list:
        file_path = videos_dir_path + "/" + file_name
        path, time_in_sec = _video_converter(file_path)
        video_list.append({
            "name": file_name,
            "path": path,
            "time": time_in_sec,
        })
    
    return video_list

def _video_converter(path):
    mp4_path = ""
    filename, extension = os.path.splitext(path)
    if extension != ".mp4" and extension != ".MP4":
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