import pdb

n=3
a = [[0] * n for _ in range(n)]
for i in range(n):
   print(a[i])
print()

r = 0
c = n//2
for i in range (1,(n*n)+1):
   a[r][c] = i 
   r = r-1
   c = c+1  
   if (r < 0 and c <= n-1 ):
      r = n-1
      
   if( c > n-1 and r >= 0):
      c = 0 

   if(r < 0 and c > n-1):
       r = r+2 
       c = c-1  

   
   if(a[r][c]!=0):
      r=r+2 
      c=c-1           

for i in range(n):
   print(a[i])
