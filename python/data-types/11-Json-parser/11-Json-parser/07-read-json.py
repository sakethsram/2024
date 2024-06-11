import json

def dump_data(data, wfd):
    keys = list(data.keys())
    print (keys)
    for key in keys:
        if (key != "userkey" and key != "product"):
            print ("{}\t{}\t{}\t{}".format(data["userkey"], data["product"], key, data[key]))
            ndata = "{},{},{},{}\n".format(data["userkey"], data["product"], key, data[key])
            wfd.write(ndata)

def main():
    fd = open("tdata.json", "r")
    wfd = open("newdata.csv", "w")
    jdata = json.load(fd) 

    for data in jdata:
        print (data)
        dump_data(data, wfd)

if (__name__ == "__main__"):
    main()
