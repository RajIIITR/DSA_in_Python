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
    
if '__main__' == __name__:
    nums = [1,1,2,3,3,4,4,8,8]
    print(find_single_element(nums))