import json
import os

from selenium_utils.navigation import scrapAllModelData

def main():
    
    parameter_file = open(f'{os.getcwd()}\parameters.json')
    params = json.load(parameter_file)  

    
    for searchSet in params:
        currentSearchSet = params[searchSet]
        args = []

        if "generation" not in currentSearchSet.keys():
            if "year" not in currentSearchSet.keys():
                print(f"Must provide at least generation or year of make. Current data set: {currentSearchSet}")
                break

        if "manufacturer" not in currentSearchSet:
            print(f"no manufacturer within current data set. Current data set: {searchSet}")
            break
        else:
            args.append(currentSearchSet.get("manufacturer"))

        if "model" not in currentSearchSet:
            print(f"no n wtihin current data set. Current data set: {searchSet}")
            break
        else:
            args.append(currentSearchSet.get("model"))

        if "generation" in currentSearchSet:
            args.append(currentSearchSet.get("generation"))

        if "year" in currentSearchSet:
            args.append(currentSearchSet.get("year"))
        
        scrapAllModelData(*args)


if __name__ == "__main__":
    main()