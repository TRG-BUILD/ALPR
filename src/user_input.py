import os

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