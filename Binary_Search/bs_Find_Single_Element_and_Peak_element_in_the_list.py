def find_single_element(nums: list) -> int:
    low = 0
    high = len(nums) - 1
    while low<=high:
        mid = (low + high) // 2
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        if (mid%2 == 1 and nums[mid] == nums[mid - 1]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):
            low = mid + 1
        else:
            high = mid - 1
    
def find_peak_element(nums: list, n: int) -> int:
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n-1] > nums[n-2]:
        return n-1
    
    low = 1
    high = n-2
    while low<=high:
        mid = (low + high) // 2
        if nums[mid - 1] < nums[mid] > nums[mid + 1]:
            return mid
        elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
            low = mid + 1
        elif nums[mid - 1] > nums[mid] > nums[mid + 1]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if '__main__' == __name__:
    nums = [1,1,2,3,3,4,4,8,8]
    n = [1,2,8,4,5,6,2,1]
    print(find_single_element(nums))
    print(find_peak_element(n, len(n)))