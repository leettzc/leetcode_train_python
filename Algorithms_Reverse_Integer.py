
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x<0-(2**31):
        return(0)
    if x>(2**31)-1:
        return(0)
    if x <0:
        absx = 0 - x
    arry = []
    dex= 1
    j = 0
    while (dex):
        n = absx//10
        m = absx-10*n
        absx = n
        if m!=0:
            j=1
        if j!=0:
            arry.append(m)
        if n==0:
            dex = 0
    outx = 0
    l=len(arry)
    print(arry)
    i=0
    while i < l:
        outx+=arry[i]*(10**(len(arry)-i-1))
        i+=1
    if x<0:
        outx = 0 - outx
    if outx<0-(2**31):
        return(0)
    if outx>(2**31)-1:
        return(0)
    return outx
print(reverse(-324))
