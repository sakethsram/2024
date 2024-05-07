fd1=open("f1.txt",'r')
fd2=open("f2.txt",'r')
c1=0
c2=0

data=fd1.readlines()
if("warning" in data):
    c1=c1+1
        

data=fd2.readline()
if("warning" in data):
    c2=c2+1


print("c1=",c1)
print("c2=",c2)
if(c2>c1):
    print("rejected")
else:
    print("accepted")    

fd1.close()
fd2.close()








