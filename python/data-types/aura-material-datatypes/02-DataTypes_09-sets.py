def main():
    engineers = {'Saketh', 'Jana', 'Vachan', 'Aura'}
    print(f"engineers   :{engineers}")

    programmers = {'Vachan', 'Sama', 'Dheer', 'Aura'}
    print(f"programmers :{programmers}")

    managers = {'Jana', 'Vachan', 'Dheer', 'Achyu'}
    print(f"managers    :{managers}")

    employees = engineers | programmers | managers           # union
    print(f"employees :{employees}")
    
    engineering_management = engineers & managers            # intersection
    print(f"engineering_management :{engineering_management}")

    fulltime_management = managers - engineers - programmers # difference
    print(f"fulltime_management :{fulltime_management}")

    engineers.add('Dilip')                                  # add element
    print(f"engineers   :{engineers}")

    print(f"employees is superset of engineers :{employees.issuperset(engineers)}") 
    print(employees)

    employees.update(engineers)         # update from another set
    print(f"employees is superset of engineers :{employees.issuperset(engineers)}") 
    print(employees)

    for group in [engineers, programmers, managers, employees]: 
        print(group)

    for group in (engineers, programmers, managers, employees): 
        group.discard('Jana')          # unconditionally remove element
    print()

    for group in (engineers, programmers, managers, employees): 
        print(group)

if (__name__ == '__main__'):
    main()
