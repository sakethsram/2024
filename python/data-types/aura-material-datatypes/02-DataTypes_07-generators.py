def generator_example1():
    ylist = list()
    for x in range(3):
        ylist.append(x*x)
    print (ylist)
 
def generator_example2():
    ylist = [x*x for x in range(3)]
    print(type(ylist))
    print(ylist)

def generator_example3():
    ylist = [x+1 for x in range(3)]
    print(ylist)

def generator_example4():
    temp_dict = {'z':x for x in range(10, 20)}
    print (temp_dict)

    temp_dict = {x:x for x in range(10, 20)}
    print (temp_dict)
    return

def generator_example5():
    print([           x    for x in range(10,20)])
    print([       str(x)   for x in range(10,20)])
    print(["aura"+str(x)   for x in range(10,20)])
    print({'aura'+str(x):x for x in range(10,20)})
    print(type({'aura'+str(x):x for x in range(10,20)}))
    return
 
def main():
    # generator_example1()
    # generator_example2()
    # generator_example3()
    # generator_example4()
    # generator_example5()
    return

if (__name__ == '__main__'):
    main()
