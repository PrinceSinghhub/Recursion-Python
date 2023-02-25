def nth_Phebonachi(num ,first,last,third):

    print(third,end=" ")
    first = last
    last = third
    third = first+last

    if num == 8:
        # print(third)
        return

    return nth_Phebonachi(num+1,first,last,third)

nth_Phebonachi(1,0,1,0)