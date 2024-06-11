import csv

def strip(src):
    flag = []
    fd1 = open(src, 'rt')
    fdata = csv.reader(fd1)
    for row in fdata:
        if len(row) > 4 and ' ' in row[4]:
            row[4] = row[4].replace(' ', '')
        if len(row) > 5 and ' ' in row[5]:
            row[5] = row[5].replace(' ', '')
        flag.append(row)
    fd1.close()
    return flag


def original(flag):
    unique = []
    with open("only-unique.csv", "w+") as fd:
        for row in flag:
            if ( row[4] == row[5]): row.pop(5)        
            t=0
            for i in unique:
                if  (row[4] == i[4] or row[4] == i[5] or row[5] == i[4] or row[5] == i[5]):
                        t = 1
                        break
            if (t==0): 
                unique.append(row)
                fd.write(','.join(map(str, row)) + '\n')
        
        return unique





sd = strip("user.csv")
flag=original(sd)

for i in flag:
    print(i)