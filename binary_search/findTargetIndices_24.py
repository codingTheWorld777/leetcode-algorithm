'''
You are given a 0-indexed integer array, sorted in non-decreasing order nums and a target element target.
A target index is an index i such that nums[i] == target.
Return a list of the target indices of nums after sorting nums in non-decreasing order.
If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

---Example 1---
Input: nums = [1,2,2,3,5], target = 2
Output: [1,2]
The indices where nums[i] == 2 are 1 and 2.

---Example 2---
Input: nums = [1,2,2,3,5], target = 3
Output: [3]
The index where nums[i] == 3 is 3.

---Example 3---
Input: nums = [1,2,2,3,5], target = 5
Output: [4]
The index where nums[i] == 5 is 4.
'''
def targetIndices(nums, target):
    low, high = 0, len(nums) - 1
    left = right = -1

    # Find the most left num that equals to target
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] == target:
            left = mid
            high = mid - 1

    # Find the most right num that equals to target
    low, high = left, len(nums) - 1
    while low <= high:
        mid = (low + high) >> 1
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        elif nums[mid] == target:
            right = mid
            low = mid + 1

    if left == -1:
        return []
    else:
        return list(range(left, right + 1))