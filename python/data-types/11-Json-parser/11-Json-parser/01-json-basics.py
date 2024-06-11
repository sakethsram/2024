import json

def basics_json_objects():
    json_obj =  {"Birds":"Parrot", "Animals":{"Wild":[{"Lion":"Asian"},{"Tiger":"BengalTiger"}]}}
    json_str = '{"Birds":"Parrot", "Animals":{"Wild":[{"Lion":"Asian"},{"Tiger":"BengalTiger"}]}}'

    print (type(json_obj))
    print (type(json_str))

    print(json_obj["Birds"])
    print(json_obj["Animals"])


def loading_json_objects_01():
    json_str = '{"Birds":"Parrot", "Animals":{"Wild":[{"Lion":"Asian"},{"Tiger":"BengalTiger"}]}}'

    a = '10'
    print (a*3)
    print (int(a)*3)

    njson_obj = json.loads(json_str)
    print(njson_obj)
    print(type(njson_obj))

def loading_json_objects_02():
    json_str = '{"Birds":"Parrot", "Animals":{"Wild":[{"Lion":"Asian"},{"Tiger":"BengalTiger"}]}}'

    try:
        print(type(json_str))

        njson_obj = json.loads(json_str)
        print(njson_obj)

        # pretty printing of json-formatted string
        print(json.dumps(njson_obj))
        print(json.dumps(njson_obj, sort_keys=True, indent=4))
        
    except (ValueError, KeyError, TypeError) as err:
        print ("JSON format error", err)

def navigating_json_object():
    json_str = '{"Birds":"Parrot", "Animals":{"Wild":[{"Lion":"Asian"},{"Tiger":"BengalTiger"}]}}'

    try:
        njson_obj = json.loads(json_str)
        print("njson_obj['Animals']                      :", njson_obj['Animals'])
        print("njson_obj['Animals']['Wild']              :", njson_obj['Animals']['Wild'])
        print("njson_obj['Animals']['Wild'][0]           :", njson_obj['Animals']['Wild'][0])
        print("njson_obj['Animals']['Wild'][0]['Lion']   :", njson_obj['Animals']['Wild'][0]['Lion'])
        print("njson_obj['Animals']['Wild'][1]['Tiger']  :", njson_obj['Animals']['Wild'][1]['Tiger'])
    except (ValueError, KeyError, TypeError) as err:
        print ("JSON format error", err)

def main():
    # basics_json_objects()
    # loading_json_objects_01()
    # loading_json_objects_02()
    # navigating_json_object()
    return()

if (__name__ == "__main__"):
    main()
    
