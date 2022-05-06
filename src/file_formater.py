

from unittest import result


def file_formater(file_path, file_format, seperator, minimum_confidence, results_list):
    new_list = combine_alpr_results_and_reduce_list(results_list, minimum_confidence)#reduce_list(results_list)
    if file_format == ".csv":
        write_to_csv(file_path, seperator, new_list)
    else:
        print("\nFilformatet: " + str(file_format) + " er ikke supporteret af file_formatter funktionen\n")
        print("Der bruges standarden som er at generere en .csv fil istedet\n")
        write_to_csv(file_path, seperator, new_list)
    

def combine_alpr_results_and_reduce_list(results_list, minimum_confidence):
    # This function takes in a results list containing all frames in the video where a result is
    # It then combines all results that point towards the same number plate
    # It does this even for partial recognitions (ie. result 1 candidate 1 with plate XXYY 
    # gets connected to result 2 candidate 4 with plate XXYY, even though result 2 candidate 1 is XXXY)
    # It then updates all the confidence values to instead be highest/lowest confidence instead + amount of "hits"
    combined_results = []
    
    for alpr_frame in results_list:
        for new_result in alpr_frame["results"]:
            result_match = None
            for new_candidate in new_result["candidates"]:
                if result_match is not None:
                    break
                result_match = _check_if_candidate_has_a_match_in_combined_results(combined_results, new_candidate)
                        
            if result_match is None:
                new_result["frames"] = 0
                new_result["start_time"] = alpr_frame["time"]
                new_result["end_time"] = alpr_frame["time"]
                new_result["average_confidence"] = new_result["candidates"][0]["confidence"]
                for candidate in new_result["candidates"]:
                    candidate["hits"] = 1
                combined_results.append(new_result)
            else:
                combined_results = _update_result(combined_results, result_match, new_result, alpr_frame["time"], minimum_confidence)
    
    return combined_results
    
def _check_if_candidate_has_a_match_in_combined_results(combined_results, new_candidate):
    # If the new candidate is found in the combined results, it returns the index to the result that has a matching candidate
    for result_index, combined_result in enumerate(combined_results):
        for prev_candidate in combined_result["candidates"]:
            if new_candidate["plate"] == prev_candidate["plate"]:
                return result_index
            
def _update_result(combined_results, result_match, new_result, frame_time, minimum_confidence):
    result_needing_update = combined_results[result_match]
    result_needing_update["frames"] += 1
    result_needing_update["end_time"] = frame_time
    
    highest_confidence_plate = None
    highest_acc_confidence = 0
    highest_confidence_hits = 0
    new_possible_candidates = []
    for old_candidate in result_needing_update["candidates"]:
        for new_candidate in new_result["candidates"]:
            if old_candidate["plate"] == new_candidate["plate"]:
                old_candidate["confidence"] += float(new_candidate["confidence"])
                old_candidate["hits"] += 1
                if old_candidate["confidence"] > highest_acc_confidence:
                    highest_acc_confidence = old_candidate["confidence"]
                    highest_confidence_plate = old_candidate["plate"]
                    highest_confidence_hits = old_candidate["hits"]
            else:
                if float(new_candidate["confidence"]) > minimum_confidence:
                    new_possible_candidates = []
            
        old_candidate["average_confidence"] = old_candidate["confidence"] / old_candidate["hits"]
        
    for possible_candidate in new_possible_candidates:
        result_needing_update["candidates"].append(possible_candidate)
        
    result_needing_update["plate"] = highest_confidence_plate
    result_needing_update["average_confidence"] = highest_acc_confidence / highest_confidence_hits
    
    combined_results[result_match] = result_needing_update
    return combined_results

def write_to_csv(file_path, seperator, results_list):
    with open(file_path, "w") as f:
        f.write("start_time" + seperator)
        f.write("end_time" + seperator)
        f.write("frames" +seperator)
        f.write("plate" + seperator)
        f.write("average_confidence" + seperator)
        f.write("\n")
        for d in results_list:
            f.write(str(d["start_time"]) + seperator)
            f.write(str(d["end_time"]) + seperator)
            f.write(str(d["frames"]) + seperator)
            f.write(str(d["plate"]) + seperator)
            f.write(str(d["average_confidence"]) + seperator)
            f.write("\n")