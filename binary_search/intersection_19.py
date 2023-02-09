"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

***Example 1:***
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

***Example 2:***
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""
# Solution 1
def intersect(nums1, nums2):
    i = j = 0
    nums1 = sorted(nums1)
    nums2 = sorted(nums2)
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1
    return res

# Solution 2
def intersect2(nums1, nums2):
    occurence, res = {}, []
    for i in range(0, len(nums1))
        if occurence[nums1[i]]:
            occurence[nums1[i]] += 1
        else:
            occurence[nums1[i]] = 1

    for j in range(0, len(nums2))
        if occurence[nums2[j]] > 0:
            res.append(nums2[j])
            occurence[nums2[j]] -= 1

    return res