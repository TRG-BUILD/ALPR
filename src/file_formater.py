

def file_formater(results_list):
    print("  TIME    :   PLATE    : CONFIDENCE")
    for d in results_list:
        print(d["time"]," : ",str(d["results"][0]["plate"]).ljust(8)," : ",d["results"][0]["confidence"])