def PrimeNumber(n,div):


    while div*div <= n:
        if n%div*div == 0:
            return "Not a Prime"

        div += 1
        PrimeNumber(n,div)


    return "Prime Number"

ans = PrimeNumber(21,2)
print(ans)