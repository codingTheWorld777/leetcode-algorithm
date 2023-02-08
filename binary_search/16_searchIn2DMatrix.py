"""
You are given an m x n integer matrix 'matrix' with the following two properties:
* Each row is sorted in non-decreasing order.
* The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

***Example 1:***
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

***Example 2:***
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    l, h = 0, m * n

    while l <= h:
        mid = (l + h) // 2
        i, j = mid // n, mid % n   # Convert to (i, j) pos from element's index

        if i < m and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            elif matrix[i][j] > target:
                h = mid - 1
        else:
            break

    return False