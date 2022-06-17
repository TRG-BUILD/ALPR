import os
import sys

def user_input():
    mi_model = get_mi_model()
    
    code = ""
    try:
        code = sys.argv[3]
    except IndexError as e:
        code = get_code(mi_model)
    
    min_confidence = get_min_confidence()
    
    file_format = get_file_format()
    seperator = get_seperator()
    
    sort_by = ""
    try:
        sort_by = sys.argv[4]
    except IndexError as e:
       sort_by = get_sorting()
    
    return code, mi_model, file_format, seperator, min_confidence, sort_by

def get_mi_model():
    print("\nDer bliver brugt OpenALPR maskin lærings algoritmen til at læse nummerplader.\n")
    return "alpr"

def get_code(mi_model):
    code = ""
    correct_choice = False
    if mi_model == "alpr":
        print("\nOpenalpr understøtter hvilken landekode nummerpladerne ligger indeni.")
        while not correct_choice:
            code = input("Koderne kan være: EU (Europa), US (USA), AU (Australien)\n").lower()
            if code != "eu" and code != "us" and code != "au":
                print("\nDu skrev: ", code, " hvilket ikke er en af mulighederne.")
                print("Skriv venligst kun 2 bogstaver som input")
            else:
                correct_choice = True
    else:
        raise Exception("Machine learning model: " + str(mi_model) + " ikke understøttet i user_input")
    
    return code

def get_min_confidence():
    confidence = 60
    print("\nDer bliver kun medtaget resultater, hvor algoritmen er mindst " + str(confidence) + "% sikker på et resultat\n")
    return confidence

def get_file_format():
    format = ".csv"
    print("\nResultaterne bliver lagt i /export_files mappen i " + format + " format\n")
    return format

def get_seperator():
    seperator = ";"
    print("\nSeperatoren mellem værdierne i output filen er " + seperator + "\n")
    return seperator

def get_sorting():
    sort_by = ""
    correct_choice = False
    print("\n Resultaterne kan sorteres efter tidsrækkefølge eller hvor sikker algoritmen er i sin vurdering")
    while not correct_choice:
        sort_by = input("Skriv venligst: tid eller vurdering\n").lower()
        if sort_by != "tid" and sort_by != "vurdering":
            print("\nDu skrev: ", sort_by, " hvilket ikke er en af mulighederne.")
            print("Skriv venligst kun en af de listede muligheder som input")
        else:
            correct_choice = True
    
    return sort_by