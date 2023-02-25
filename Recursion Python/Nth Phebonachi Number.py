def NthPhebonachi(n):

    if n<2:
        return n

    return NthPhebonachi(n-1) + NthPhebonachi(n-2)

res = NthPhebonachi(5)
print(res)