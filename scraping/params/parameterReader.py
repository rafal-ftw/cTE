import json
import os


parameter_file = open(f'{os.getcwd()}\scraping\params\parameters.json')
data = json.load(parameter_file)

for key in data:

    print(f"current dictionary we're working on is: {data[key]}")

    currentDict = data[key]

    print(currentDict["manufacturer"])
    
    print(currentDict["model"])
    
    print(currentDict["generation"])