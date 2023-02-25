import math as m
def phebonachi(n):
    formula = int(m.pow((1 + m.sqrt(5)) / 2, n) / m.sqrt(5))
    return formula

n = int(input("Enter Number: "))
ans = phebonachi(n)
print(ans)
