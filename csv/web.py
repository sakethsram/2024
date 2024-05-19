import csv

def strip(src):
    datalist = []
    with open(src, 'rt') as fd:
        fdata = csv.reader(fd)
        for row in fdata:
            datalist.append(row)
    return datalist

def count_ret_code(dl):
    with open("new-web-req.csv", "w+") as fd:
        all = []
        unique = []
        final = []

        for row in dl:
            all.append(row[5])
        
        # Remove the header
        all.pop(0)  

        for code in all:
            if code not in unique:
                unique.append(code)

        print(unique)

        for i in unique:
            c = all.count(i)
            final.append([i, c])
            fd.write(f'{i},{c}\n')
        
        print(final)

dl = strip("web-req.csv") 
count_ret_code(dl)
