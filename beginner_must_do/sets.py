a=[25,56,87,14,36,78,5,7,8,9]
b=[56,11,4,36,1,2,3,6,23 , 8]
print("a=",a)
print("b=",b)

    


def sets():
    u=a+b
    u.sort()    
    print("union c = ",u)
            
    
    i = []
    for flag in u:
        if flag in a and flag in b: i.append(flag) 
    print(i)    

    

    a_b = []
    for e in a:
        if e not in b:
            a_b.append(e)
    print("a-b=", a_b)

    b_a = []
    for f in b:
        if f not in a:
            b_a.append(f)
    print("b-a=", b_a)

    disjoint = []
    for x in u:
        if x not in i:
            disjoint.append(x)
    print("d=disjoint set =", disjoint)


sets()
