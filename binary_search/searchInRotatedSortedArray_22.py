"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

***Example 1:***
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

***Example 2:***
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
"""
def search(nums, target):
    l, r = 0, len(nums) - 1
    pivot = findPivot(nums)
    left_nums = binarySearch(nums, target, l, pivot - 1)
    right_nums = binarySearch(nums, target, pivot, r)

    return max(left_nums, right_nums)

# Find the pivot of a rotated sorted array: Index of the minimum number in the array
def findPivot(nums):
    l, r = 0, len(nums) - 1
    if len(nums) == 1 or (nums[l] < nums[r]):
        return 0

    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return l

# Classic binary search (apply for the left (pos:beginning to pivot - 1) and right (pos:pivot to end) array
def binarySearch(nums, target, l, r):
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1