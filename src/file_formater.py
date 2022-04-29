

def file_formater(file_path, file_format, seperator, results_list):
    new_list = reduce_list(results_list)
    if file_format == ".csv":
        write_to_csv(file_path, seperator, new_list)
    else:
        raise Exception("Fileformat: " + str(file_format) + " not supported in file_formater")
    
def reduce_list(results_list):
    new_results = []
    current_result = {
        "plate": None
    }
    for d in results_list:
        if current_result["plate"] != d["results"][0]["plate"]:
            if current_result["plate"] is not None:
                current_result["end_time"] = d["time"]
                new_results.append(current_result)
            current_result = {
                "start_time": d["time"],
                "end_time": "",
                "plate": d["results"][0]["plate"],
                "lowest_confidence": float(d["results"][0]["confidence"]),
                "highest_confidence": float(d["results"][0]["confidence"])
            }
        else:
            if current_result["lowest_confidence"] > d["results"][0]["confidence"]:
                current_result["lowest_confidence"] = d["results"][0]["confidence"]
            if current_result["highest_confidence"] < d["results"][0]["confidence"]:
                current_result["highest_confidence"] = d["results"][0]["confidence"]

    current_result["end_time"] = d["time"]
    new_results.append(current_result)

    return new_results

def write_to_csv(file_path, seperator, results_list):
    with open(file_path, "w") as f:
        f.write("start_time" + seperator)
        f.write("end_time" + seperator)
        f.write("plate" + seperator)
        f.write("lowest_confidence" + seperator)
        f.write("highest_confidence" + seperator)
        f.write("\n")
        for d in results_list:
            f.write(str(d["start_time"]) + seperator)
            f.write(str(d["end_time"]) + seperator)
            f.write(str(d["plate"]) + seperator)
            f.write(str(d["lowest_confidence"]) + seperator)
            f.write(str(d["highest_confidence"]) + seperator)
            f.write("\n")