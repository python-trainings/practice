import json
f = open("data.json")
d = json.load(f)

if  d["web-app"]["servlet"][4]["init-param"]["dataLog"] == 1:
	print "Is good"
else:
	print "bad.................."