# # --------------JSON------------------
# {
# 	"name" : "Pradip",
# 	"lname" : "Das",
# 	"address" : " blore",
# 	"id" : 1
# }
# # -------------YAML-----------------
# "data" :
#   "name" : "Pradip"
#   "lname" : "das"
#   "address" : "blore"
#   "id" : 1
# #------------XML-----------------------
# <data>
#     <name>Pradip</name>
#     <lname>Das</lname>
#     <address>blore</address>
#     <id>1</id>
# </data>
# # ----------------------------------
import json
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
d = {
	"name" : "Pradip",
	"lname" : "Das",
	"address" : " blore",
	"id" : 1	
}
d["age"] = {"year" : 90, "month" : 8, "time" : {"HH" : 12}}

for i in range(5):
	d["data" + str(i)]  = i
f = open("data.json","w")
json.dump(d,f)
f.close()

f = open("data.yaml","w")
yaml.dump(d,f)
f.close()




