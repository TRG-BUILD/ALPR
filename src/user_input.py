import os

def user_input():
    mi_model = "alpr"
    
    code = get_code(mi_model)
    
    file_format = ".csv"
    seperator = ";"
    
    return code, mi_model, file_format, seperator

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