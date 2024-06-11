import json

# str --> json
def str_to_json():
    json_obj = json.loads('{"name" : "Aura", "Location" : "Karnataka"}')
    print(json_obj)

# file --> json
def load_json_from_file():
    json_file = 't.json'
    
    fd = open(json_file)
    
    json_obj = json.load(fd)
    
    fd.close()

    print(json_obj)
    print()
    
    print(json_obj['Id'])

# file --> json --> str --> json
def json_to_str_to_json():
    json_file = 't.json'
    fd = open(json_file)
    json_obj = json.load(fd)
    fd.close()

    # print (json.dumps(json_obj, sort_keys=True, indent=4))

    json_decoded = json.dumps(json_obj)
    print(type(json_decoded))
    print (json_decoded)

    encoded_data = json.loads(json_decoded)

    print(type(encoded_data))
    print(encoded_data)
    print(encoded_data['Id'])
    return

def main():
    # str_to_json()
    # load_json_from_file()
    # json_to_str_to_json()
    return()

if (__name__ == "__main__"):
    main()
    
