import json
import os
import selenium_utils.globals as globals

from selenium_utils.navigation import scrapAllModelData

def main():
    
    parameter_file = open(f'{os.getcwd()}\scraping\parameters.json')
    params = json.load(parameter_file)  

    globals.initialize()
    
    for searchSet in params:
        currentSearchSet = params[searchSet]
        args = []

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