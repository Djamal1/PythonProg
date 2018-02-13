import json

class j_Obj(object): 
	pass

myJson = j_Obj()
myJson.content = {}
myJson.content["log"] = "LOL"
myJson.content["pass"] = "12345"

f = open("data_base2.txt", "w")

json.dump(myJson.content, f)
f.close()
f = open("data_base2.txt", "r")
j_Obj = json.load(f)
print(j_Obj["log"])
f.close()