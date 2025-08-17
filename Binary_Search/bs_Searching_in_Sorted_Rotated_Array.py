def S_Rotated_Array_Unique_Element(nums: list, target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

if '__main__' == __name__:
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(S_Rotated_Array_Unique_Element(nums, target))