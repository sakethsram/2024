fd=open("a.txt", "r" )
count=0
l = fd.readline()
while( len(l) != 0):
    if "warning" in l: count=count+1        
    l = fd.readline()

print(count)
fd.close()
