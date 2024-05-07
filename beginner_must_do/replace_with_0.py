a=[3,2,6,3,8]    
print("len = ",len(a))
n=len(a)
print("before :",a)

for i in range(n-1):
    j=i+1
    for j in range(j,n):
        if a[i]==a[j]:
            a[j]=0

print("after:",a)
