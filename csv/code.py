import csv

def strip(src):
    datalist = []
    fd1 = open(src, 'rt')
    fdata = csv.reader(fd1)
    for row in fdata:
        if len(row) > 4 and ' ' in row[4]:
            row[4] = row[4].replace(' ', '')
        if len(row) > 5 and ' ' in row[5]:
            row[5] = row[5].replace(' ', '')
        datalist.append(row)
    fd1.close()
    return datalist

def unique(datalist):
    unique_list = []
    for i in range(len(datalist)):
        if datalist[i][4] == datalist[i][5]:
            del datalist[i][5]
        unique_list.append(datalist[i])
        for j in range(i + 1, len(datalist)):
            if not (datalist[i][4] == datalist[j][4]) or (datalist[i][4] == datalist[j][5]) or ((datalist[i][5] == datalist[j][4] or datalist[i][5] == datalist[j][5])):
                unique_list.append(datalist[j])

    
    
    

    fd2 = open("new.csv", "w", newline='')
    for row in unique_list:
         fd2.write(','.join(row) + '\n')
    fd2.close()

strip_data = strip("user.csv")

for row in strip_data:
    print(row)

unique(strip_data)
