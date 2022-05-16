import os
from time import time

from file_formater import file_formater
from user_input import user_input
from video_loader import video_loader
from recognizer import recognizer

def controller():
    raise Exception("HERE")
    videos_dir_path = os.getcwd() + "/input_videos"
    files_dir_path = os.getcwd() + "/export_files"
    video_list = video_loader(videos_dir_path)
    if len(video_list) == 0:
        print("\nIngen videoer er blevet lagt i /alpr/input_videos/ folderen.")
        print("\nVideoer vil blive konverteret til mp4 hvis de ikke er det, hvilket kan reducere kvaliteten.\n")
        return False
    else:
        print("\nInput modtaget korrekt for videoene:")
        for video in video_list:
            print(str(video["name"])) 
        print("\nAlle videoer i korrekt mp4 format. Indtast venligst de konfigurationer du ønsker\n")
    
    code, mi_model, file_format, seperator, minimum_confidence, sort_by = user_input()
    print("\nKører plade genkendelses algoritmen for en af gangen. Vær venligst tålmodig!")
    print("\nDet vil normalt tage mange gange videoens længde at analysere for algoritmen")
    print("\nDette er påvirket primært af hvor god din computer er og kvaliteten af videoen")
    
    for video in video_list:
        start_time = time()
        print("\nPåbegynder plade genkendelses algoritmen på filen " + video["name"] + "\n")
        result_list = recognizer(code, mi_model, video["path"], video["time"])        
        print("\nAlgoritmen er færdig, gemmer som fil\n")
        file_path = files_dir_path + "/" + video["name"].replace(".mp4",file_format).replace(".MP4", file_format)
        file_formater(file_path, file_format, seperator, minimum_confidence, sort_by, result_list)
        end_time = time()
        print("\nFil gemt som " + str(video["name"]).replace(".mp4", file_format) +" i /alpr/export_files/ folderen.\n")
        print("\nDet tog " + str(round(end_time-start_time, 2)) + " sekunder.\n")
    print("\nAlle videoer er blevet analyseret. Se i README.md filen under 'Analysis' sektionen, hvad de forskellige kolonnner i filerne betyder.")
    return True
    
if __name__ == '__main__':
    controller()