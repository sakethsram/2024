import json

#creating list of JSON objects
'''
[
   {"name" : "aura", "age" : 10},
   {"name" : "aura", "age" : 20},
   {"name" : "aura", "age" : 30}
]
'''

def sample_json_build():
    nd_obj = {"name": "lokesh"}
    print (nd_obj)

    a = "name"
    b = "lokesh"
    nd_obj = {a:b}
    print (nd_obj)

def build_json_from_static_values():
    jdata = []
    ldata = [10, 20, 30]
    t = {"name":"aura", "age":ldata[0]}
    jdata.append(t)

    t = {"name":"aura", "age":ldata[1]}
    jdata.append(t)

    jdata.append({"name":"aura", "age":ldata[2]})

    print(jdata)
    print(jdata[0]['name'], jdata[0]['age'])
    print(jdata[1]['name'], jdata[1]['age'])
    print(jdata[2]['name'], jdata[2]['age'])

def build_json_from_static_values_dynamic():
    jdata = []
    ldata = [10, 20, 30]
    lnames = ["Python", "C", "R"]
    """
    [
        {"BName" : "Python", "page_count" : 10 },
        {"BName" : "C", "page_count" : 20 },
        {"BName" : "R", "page_count" : 30 }
    ]
    """

    i = 0
    while(i < len(ldata)):
        jdata.append({"BName":lnames[i], "page_count":ldata[i]})
        i = i + 1

    print(jdata)

def json_to_file():
    """
    fd = open("jdata.json", "w")
    json.dump(jdata, fd, indent=2)
    fd.close()
    """
    jdata = []
    ldata = [10, 20, 30]
    lnames = ["Python", "C", "R"]

    i = 0
    while(i < len(ldata)):
        jdata.append({"BName":lnames[i], "page_count":ldata[i]})
        i = i + 1

    with open("jdata.json", "w") as fd:
        json.dump(jdata, fd, indent=4)

def main():
    # sample_json_build()
    # build_json_from_static_values()
    # build_json_from_static_values_dynamic()
    json_to_file()
    return()

if (__name__ == "__main__"):
    main()
    
