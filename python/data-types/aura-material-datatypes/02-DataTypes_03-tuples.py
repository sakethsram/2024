def tuples_basics():
    tA = (123, "abcdef")
    tB = (345, 'abb')

    print(f"Tuple length         :{len(tA)}")

    tA = (123, 12)
    print(f"Max value element tA :{max(tA)}")
    print(f"min value element    :{min(tA)}")
    #Q. Get index of minimum value?
    #Q. What happens to max() and min() if tuple cosists int and strings
    #Q. Is list has max() and min()?

    tC = tB + tuple('823')
    print(tC)

    tC = tB + tuple([823])
    print(tC)

    tB = tB + tuple("823")
    print(tB)
    # tB = (345, 'abb', "823") #Expected
    # tB = (345, 'abb', '8', '2', '3') #Actual
    
    #Q. Add a string '823' to tuple

    print("")
    tlist = [123, 'xyz', 'zara', 'abc']
    ttuple = tuple(tlist)
    print(f"Tuple elements :{ttuple}")
    return

def tuples_operations_01():
    tA = ('1', 98346)
    tB = (345, 'abb')
    # tA[0] = 100
    # tA.append(4)

    # del tA
    print(f"tA  :{tA}")
    
    tC = tB + tA + tB + (2, 3, 4, 5)
    print(f"tC  :{tC}")

    tC = tB + tA + tB + tuple([5, 8, 9, 2])
    print(f"tC  :{tC}")

    tC = tC + tA

    temp = (10, 20)
    a, b = temp
    print (a)
    print (b)

def tuples_operations_02():
    IndiasSon = ("Subhash", "Bose", 1897, "Azad Hind Fauj", 1942, "War", "Cuttack, Bengal Presidency")
    print(IndiasSon)
    name, surname, b_year, military, m_year, profession, b_place = IndiasSon
    print(name, surname, b_place)

    print("")
    months = (' ', 'January','February','March','April','May','June', 'July','August','September','October','November','December')
    print(f"months :{months}")

    print("")
    x = 8
    print(months[x])
    print(len(months))

    # months.sort()
    print(f"months :{months}")
    return

def main():
    # tuples_basics()
    # tuples_operations_01()
    tuples_operations_02()
    return

if __name__ == "__main__":
    main()