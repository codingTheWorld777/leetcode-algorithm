"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

***Example 1:***
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

***Example 2:***
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
"""
def findKthPositive(arr, k):
    i = 1
    missing_nums_list = []

    while True:
        if i not in arr:
            missing_nums_list.append(i)
        i += 1

        if len(missing_nums_list) > k:
            break

    return missing_nums_list[k - 1]