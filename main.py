import os
import subprocess
import json
import ffmpeg
from math import floor

DEBUG = 1

def user_input():
    correct_choice = False
    
    print("\nSkriv hvilken kode nummerpladerne ligger indeni.")
    while not correct_choice:
        code = input("Koderne kan være: EU, US, AU\n").lower()
        if code != "eu" and code != "us" and code != "au":
            print("\nDu skrev: ", code, " hvilket ikke er tilladt.")
        else:
            correct_choice = True
            
    correct_choice = False
    print("\nCopy paste stien til det billede eller den video der skal analyseres")
    while not correct_choice:
        path = input("Husk at tilfoej hele stien, inklusiv filen du vil have\n")
        if not os.path.isfile(path):
            print("\nDu skrev: ", path, " hvilket ikke peger paa en specifik fil")
        else:
            correct_choice = True
    
    return code, path

def find_plates(code, path):
    return subprocess.run(["alpr","-c",code,path,"-n","1000", "--json"], stdout=subprocess.PIPE)

def convert_video(path):
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

def clean_result(stdout_string):
    bytes = stdout_string.replace(b"\r",b"")
    bytes = bytes.replace(b"\n",b"")
    string_with_multiple_jsons = bytes.decode('utf-8')
    
    list_of_jsons = []
    cur_json_str = ""
    scope = 0
    for s in string_with_multiple_jsons:
        cur_json_str += str(s)
        
        if s == "{":
            scope += 1
        elif s == "}":
            scope -= 1
            if scope == 0:
                list_of_jsons.append(json.loads(cur_json_str))
                cur_json_str = ""
    
    return list_of_jsons

def _convert_sec_to_timestamp(time_in_sec):
    time_in_sec = int(time_in_sec)
    hour = floor(time_in_sec / 3600)
    time_in_sec -= hour * 3600
    min = floor(time_in_sec / 60)
    time_in_sec -= min * 60
    sec = floor(time_in_sec  / 1)
    
    return str(hour).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2)

def retrieve_results(pred_list, vid_time_length, vid_frame_length):
    results = []
    frame = 0
    
    for d in pred_list:
        frame += 1
        if len(d["results"]) != 0:
            time = (frame / vid_frame_length) * vid_time_length
            d["time"] = _convert_sec_to_timestamp(time)
            results.append(d)
    
    return results


if __name__ == '__main__':
    # Start with getting some user input
    if DEBUG == 1:
        code, path = user_input()
    else:
        code, path = "eu", "C:\\Users\\Martin\\projects\\build\\alpr\\alprVideos\\TH Sauers Vej\\00004.MTS"
        
    # Then check if the file is in an accepted format (mp4 for video, jpg or png for pictures)
    # Convert the video to mp4 if it is in another format
    path, length_of_vid = convert_video(path)

    # Make predictions. Presently, only alpr is supported, but can be changed here
    # All 3 functions are coupled to alpr, given it returns each frame as a json (others might not)
    # The first predicts on each frame and returns that as a byte string of these predictions (most have no results)
    # The second converts the bytestring into a list of json objects
    # The third retrieves only those frames with results, and gives a timestamp in the video
    predictions = find_plates(code, path)
    list_of_dicts = clean_result(predictions.stdout)
    results = retrieve_results(list_of_dicts,length_of_vid,len(list_of_dicts))
    
    print("  TIME    :   PLATE    : CONFIDENCE")
    for d in results:
        print(d["time"]," : ",str(d["results"][0]["plate"]).ljust(8)," : ",d["results"][0]["confidence"])