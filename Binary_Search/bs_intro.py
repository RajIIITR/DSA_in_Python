def bs_iterative(low: int, high: int, target: int, arr: list) -> int:
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def bs_recursion(low: int, high: int, target: int, arr: list) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return bs_recursion(mid + 1, high, target, arr)
    else:
        return bs_recursion(low, mid - 1, target, arr)
    
if '__main__' == __name__:
    arr = [1, 2, 3, 4, 5]
    print(bs_iterative(0, len(arr) - 1, 3, arr))
    print(bs_recursion(0, len(arr) - 1, 3, arr))