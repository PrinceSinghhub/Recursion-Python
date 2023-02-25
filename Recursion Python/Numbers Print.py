'''Q print a numbers() 5 time without call more then time our function externally and
        with out modify function code;
        output = 1 2 3 4 5'''

def numbers1(n):
    print(n)
    numbers2(2)

def numbers2(n):
    print(n)
    numbers3(3)

def numbers3(n):
    print(n)
    numbers4(4)

def numbers4(n):
    print(n)
    numbers5(5)

def numbers5(n):
    print(n)

numbers1(1)
