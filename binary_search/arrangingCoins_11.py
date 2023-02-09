"""
You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

***Example 1:***
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

***Example 2:***
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
"""
def arrangeCoins(n):
    l, h = 0, n
    row_complete = 0

    while l <= h:
        row_md = (l + h) // 2
        coins_needed = row_md * (row_md + 1) / 2
        if coins_needed > n:
            h = row_md - 1
        else: # enough coins, go higher
            l = row_md + 1
            row_complete = row_md
    return row_complete

# Second solution
def arrangeCoins2(n):
    count_row, coins = 1, n - 1
    while coins > count_row:
        count_row += 1
        coins -= count_row

    return count_row