import subprocess
import json
from math import floor

def recognizer(code, path, length_of_vid):
    # Make predictions. Presently, only alpr is supported, but can be changed here
    # All 3 functions are coupled to alpr, given it returns each frame as a json (others might not)
    # The first predicts on each frame and returns that as a byte string of these predictions (most have no results)
    # The second converts the bytestring into a list of json objects
    # The third retrieves only those frames with results, and gives a timestamp in the video
    predictions = find_plates(code, path)
    list_of_dicts = clean_result(predictions.stdout)
    return retrieve_results(list_of_dicts,length_of_vid,len(list_of_dicts))


def find_plates(code, path):
    return subprocess.run(["alpr","-c",code,path,"-n","1000", "--json"], stdout=subprocess.PIPE)

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