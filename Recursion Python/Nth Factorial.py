def nthFactorial(n,ans):

    if n == 0:
        return ans

    ans*=n
    return nthFactorial(n-1,ans)

a = 5
ans = nthFactorial(a,1)
print(ans)
