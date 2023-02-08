"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

***Example 1:***
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

***Example 2:***
Input: grid = [[3,2],[1,0]]
Output: 0
"""
# What about O(m + n) solution?
def countNegatives(grid):
    # Complexity = O(mlog(n))
    count_negative = 0
    num_rows = len(grid[0])

    for i in range(0, len(grid)):
        l, h = 0, len(grid[0]) - 1
        last_negative_num = num_rows
        while l <= h:
            mid = (l + h) // 2

            if grid[i][mid] >= 0:
                l = mid + 1
            elif grid[i][mid] < 0:
                count_negative += last_negative_num - mid
                h = mid - 1
                last_negative_num = mid

    return count_negative