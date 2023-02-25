# Q print 1 to 5 using recursion

def PrintNumbers(n):

    # todo base case where function stop now
    if(n==5):
        print(n)
        return

    print(n)
    PrintNumbers(n + 1)

PrintNumbers(1)