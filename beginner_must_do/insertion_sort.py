a=[8,9,1,4,5,6,2]
print(a)
n=len(a)
i=1
for i in range(1,n):
    flag=a[i]
    for k in range(i-1,-1,-1):
        if(a[k]>a[k+1]):
            a[k],a[k+1]=a[k+1],a[k]
        else:
            break

print(a)
                
