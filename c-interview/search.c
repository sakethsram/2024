#include<stdio.h>
int a[] = {1, 4, 5, 7, 9, 12, 15, 18, 19, 22, 25, 29, 40, 50};
int bin(int t)
{
    int l=0,h=13;
    int m;
    while(l<=h)
    {       
        m=(l+h)/2;      
        if(a[m]==t)
        {
            printf("\nfound at %d\n",m)        ;
            return m;
        }
        else if(a[m]>t)
            h=m-1;
        else if(a[m]<t)
            l=m+1;
    }
    printf("\n not found \n");
    return 0 ;     
}

void main()
{
    bin(1111    );
}