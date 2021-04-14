import json
dictionary={
    "name" : "Sahib",
    "State" : "Raj",
    "code" : 88,
    "phonenumber" : "85792963395"
}
json_obj = json.dumps(dictionary, indent = 4)

with open("sample.json","w") as outfile:
       outfile.write(json_obj)