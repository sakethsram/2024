def test_fun1():
    #....
    #....
    x = 5

    #....
    #....
    y = 10

    #....
    #....
    z = 20

    #....
    #....

    return x, y, z

def test_fun2():
    #....
    # x = 5
    yield 5

    #....

    # y = 10
    yield 10

    #....

    # z = 20
    yield 20
    print ("")

    #return (x, y, z)
    return

def gen_yield_basic():
    #....
    yield 15

    #....
    yield "temp"

    #....
    yield 'a'
    print ("")

def get_new_generator():
    t1 = range(5)
    print(f"1. t1 :{type(t1)}")

    t2 = list(range(5))
    print ("2. mylist type :", type(t2))
    print(t2)

    for i in t2:
        yield i*i
    return

def fib(n):
    pre, cur, nxt, i = -1, 1, 0, 1

    while (i <= n): 
        prev = cur
        cur =  nxt
        nxt = prev + cur
        yield cur
        i = i + 1

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, number-1, 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes_without_yield(input_list):
    result_list = list()

    for element in input_list:
        if (is_prime(element)):
            result_list.append(element)

    return result_list

def get_primes_with_yield(input_list):
    for element in input_list:
        if (is_prime(element)):
            yield element

def get_primes_with_filter(input_list):
    retval = filter(is_prime, input_list)
    print(type(retval))
    print(retval)
    return list(retval)

def main():
    a, b, c = test_fun1()
    print(f"a :{a}, b :{b}, c :{c}")
    
    a, b, c = test_fun2()
    print(f"a :{a}, b :{b}, c :{c}")

    a, b, c = gen_yield_basic()
    print(f"a :{a}, b :{b}, c :{c}")

    tlist = list(gen_yield_basic())
    print (tlist)

    gen_obj = gen_yield_basic()
    print (type(gen_obj))
    print (gen_obj)

    for item in gen_yield_basic():
        print(item)

    mygen = get_new_generator()
    print ("3. ", type(mygen))
    print ("4. ", list(mygen))

    for i in mygen:
        print(" ===", i)
    print ("5. ", list(mygen))

    flist = list(fib(10))
    print(flist)
    print(flist)

    num_list = [2, 5, 7, 8, 11, 15, 23, 29]
    print (num_list)
    result = get_primes_without_yield(num_list)
    print(result)

    print("type of result ", type(result))

    result = get_primes_with_yield(num_list)
    print(result)
    #print(dir(result))
    print(list(result))

    result = get_primes_with_filter(num_list)
    print(list(result))
    return

if (__name__ == '__main__'):
    main()

