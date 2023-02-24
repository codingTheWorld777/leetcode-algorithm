'''
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.
In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.

---Example 1---
Input: nums = [-2,-1,-1,1,2,3]
Output: 3
Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.

---Example 2---
Input: nums = [-3,-2,-1,0,0,1,2]
Output: 3
Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.

---Example 3---
Input: nums = [5,20,66,1314]
Output: 4
Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.
'''
def maximumCount(nums):
    if len(nums) == 1:
        return 0 if nums[0] == 0 else 1
    else:
        l, h = 0, len(nums) - 1
        left = right = -1

        # Find the most right indice of negative number
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] >= 0:
                h = mid - 1
            elif nums[mid] < 0:
                l = mid + 1
                right = mid

        # Find the most left indice of positive number
        l, h = right + 1, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == 0:
                l = mid + 1
            elif nums[mid] > 0:
                left = mid
                h = mid - 1

        if left == -1 and right == -1:
            return 0
        else:
            if left == -1:
                return right + 1
            elif right == -1:
                return len(nums) - left
            else:
                return max(right + 1, len(nums) - left)