def lb(arr: list, target: int, n: int) -> int:
    """
    Returns the index of the first element greater than or equal to the target.
    """
    low = 0
    high = n-1
    ans = n 
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= target:
            ans = mid
            high = mid -1
        else:
            low = mid + 1
    return ans

if '__main__' == __name__:
    arr = [1, 2, 4, 4, 6, 8, 9, 9]
    print(lb(arr, 5, len(arr))) # Output: 4