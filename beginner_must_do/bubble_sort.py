a=[8,9,1,4,5,6,2]
n=len(a)
print("before",a)
for i in range(n):    
    for j in range(i+1,n):
        
        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]

print(a)