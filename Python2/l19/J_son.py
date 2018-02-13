import json

f = open("data_base.txt", "r")
jsonObj = json.load(f)
print(jsonObj)