"""
Given an array arr of integers, check if there exist two indices i and j such that :
* i != j
* 0 <= i, j < arr.length
* arr[i] == 2 * arr[j]

***Example 1:***
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

***Example 2:***
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""
# Need to find another solution with O(log(n))
def checkIfExist(arr):
    arr_ = sorted(arr)
    l, h = 0, len(arr_) - 1
    while l <= h and h > 0:
        if arr_[h] > 0:
            num = float(arr_[h]) / 2
            if num == arr_[l]:
                return True
            elif num > arr_[l]:
                l = l + 1
            elif num < arr_[l]:
                h = h - 1
                l = 0
                continue
        elif arr_[h] < 0:
            num = float(arr_[l]) / 2
            if arr_[h] == num:
                return True
            elif arr_[h] > num:
                l = l + 1
            elif arr_[h] < num:
                h = h - 1
                l = 0
                continue
        elif arr_[h] == 0 and l != h:
            if arr_[h] == arr_[l] / 2:
                return True
            else:
                h = h - 1
                l = 0
                continue
    return False