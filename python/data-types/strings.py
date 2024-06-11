def string_split():
    #String with tabs, single space and multiple spaces
    #a = "970 2          09      6     7    5   6//**-965320              "
    #print(a)
    #print(a.split())
    #print(a.split()[1])
    #print("".join(a.split()))
    
    #print("-".join(a.split()))
    #print(" ".join(a.split()))
    #print(a)

    #tstr = "     Aura Networks     Bengaluru   "
    #print(" ".join(tstr.split()))

    #print("")
    tstr = "     Aura Networks  \n  Bengaluru\n         India  "
    print(tstr)
    print("plain split =",tstr.split())
    #print(tstr.split(' '))
    print(tstr.split(' ', 1))
    print(tstr.split(' ', 2))
    #print(tstr.split('\n'))

    #print("")
    #email = "bhagavanprasad@gmail.com"
    #print(email)
    #print(email.split('@'))

    #username = email.split('@')[0]
    #dname = email.split('@')[1]
    #print(username)
    #print(dname)

    #a, b = [10, 20]
    #username, dname = email.split('@')
    #print(username)
    #print(dname)
    return


string_split()