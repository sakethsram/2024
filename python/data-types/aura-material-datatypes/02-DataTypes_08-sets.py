def basic_operations_on_set():
    my_set = {1, 2, 3, 8, 4}
    print(type(my_set))
    print(my_set)

    # set of mixed datatypes
    my_set = {1.0, "Hello", (1, 2, 3)}
    print(my_set)

    # my_set = {1.0, "Hello", (1, 2, 3), {6, 7, 8}}
    # print(my_set)

    tlist = [7, 1, 2, 3, 2, 5]
    print(tlist)
    
    my_set = set(tlist)
    print(type(my_set))
    print(my_set)

    a = {}
    print(type(a))

    a = set()
    print(type(a))

    my_set = {1, 2, 3}
    print(my_set)

    my_set.add(5)
    my_set.add(0)
    print(my_set)

    my_set.update([2, 3, 4])
    print(my_set)

    my_set.update([4, 5], {1, 6, 8}, (9, 10))
    print(my_set)

    print("")
    my_set = {1, 3, 4, 5, 6}
    print(my_set)

    my_set.discard(3)
    print(my_set)

    my_set.remove(6)
    print(my_set)

    my_set.discard(2)
    print(my_set)

    # my_set.remove(2)
    print(my_set)
    print("")

    my_set = set("HelloWorld")
    print(my_set)

    print(my_set.pop())
    print(my_set)

    my_set.pop()
    print(my_set)

    my_set.discard('l')
    print(my_set)

    my_set.clear()
    print(my_set)

    print("")
    return

def set_operations():
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8, 9}
    print("A ", A)
    print("B ", B)
    print(f"A | B -->{A | B}")
    print(A.union(B))
    print(B.union(A))
    print("")

    print(A & B)
    print(A.intersection(B))
    print(B.intersection(A))
    print("")

    print(A - B)
    print(A.difference(B))
    print("")

    print(B - A)
    print(B.difference(A))
    print("")

    print(A ^ B)
    print(A.symmetric_difference(B))
    print("")

    print(B ^ A)
    print(B.symmetric_difference(A))
    print("")
    return

def main():
    # basic_operations_on_set()
    # set_operations()
    return

if (__name__ == '__main__'):
    main()
