def mul(mid: int, n: int, m: int):
    ans = 1
    for i in range(1,n+1):
        ans = ans * mid
        if (ans > m):
            return 2
    if ans == m:
        return 1
    else:
        return 0
    
def NthRoot(n: int, m: int):
    low = 1 
    high = m
    while low<=high:
        mid = (low + high) // 2
        midn = mul(mid, n, m)

        if midn == 1:
            return mid
        elif midn == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if '__main__' == __name__:
    nums = 1000
    print(NthRoot(3 ,nums))