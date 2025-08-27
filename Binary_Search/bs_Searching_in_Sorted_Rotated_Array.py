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

def S_Rotated_Array_Duplicate_Element(nums: list, target: int) -> bool:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high - low) // 2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        
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
    
    return False

def find_min_Rotated_Sorted_Array(nums: list):
    low = 0
    high = len(nums) - 1
    mn = 100
    while low<=high:
        mid = (low + high) // 2
        if nums[low] < nums[mid]:
            mn = min(mn, nums[low])
            low = mid + 1
        else:
            mn = min(mn, nums[mid])
            high = mid - 1
    return mn

if '__main__' == __name__:
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums_D = [3, 1, 1]
    nums_R = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(S_Rotated_Array_Unique_Element(nums, target))
    print(S_Rotated_Array_Duplicate_Element(nums_D, target))
    print(find_min_Rotated_Sorted_Array(nums_R))