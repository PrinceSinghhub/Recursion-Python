def RecursionBS(myarr,target,start,end):

    mid = start + (end-start)//2

    if(start>end):
        return -1

    if(target==myarr[mid]):
        return mid

    if target>myarr[mid]:
        return RecursionBS(myarr,target,mid+1,end)

    return RecursionBS(myarr, target, start,mid-1)


arr = [1,2,6,9,10,15,18]
ans = RecursionBS(arr,18,0,len(arr)-1)
print(ans)