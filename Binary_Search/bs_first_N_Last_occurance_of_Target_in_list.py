from typing import List

def firstOccurance(nums: List, target: int) -> int:
    """
    This function returns the index of the first occurrence of the target number in the given list of numbers
    """
    low = 0
    high = len(nums) - 1
    first = -1
    while low<=high:
        mid = (low + high) // 2
        if nums[mid] == target:
            first = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def LastOccurance(nums: List, target: int) -> int:
    low = 0
    high = len(nums) - 1
    last = -1
    while low<=high:
        mid = (low + high) // 2
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = firstOccurance(nums, target)
        if first == -1:
            return [-1, -1]
        last = LastOccurance(nums, target)
        return [first, last]
    
if "__main__" == __name__:
    nums = [5,7,7,8,8,10]
    target = 8
    print(Solution().searchRange(nums, target))