"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

***Example 1:***
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

***Example 2:***
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

***Example 3:***
Input: nums = [], target = 0
Output: [-1,-1]
"""
def searchLeftOrRightPos(left_or_right, nums, target):
    """
    :type left_or_right in [0, 1]
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    l, h = 0, len(nums) - 1
    pos = -1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            h = mid - 1
        elif nums[mid] == target:
            if left_or_right == 0:      # search for left pos
                pos = mid
                h = mid - 1
            elif left_or_right == 1:   # search for right pos
                pos = mid
                l = mid + 1
    return pos

def searchRange(nums, target):
    return [searchLeftOrRightPos(0, nums, target), searchLeftOrRightPos(1, nums, target)]