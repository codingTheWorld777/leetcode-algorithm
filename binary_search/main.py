# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    def kWeakestRows(mat, k):
        m, n = len(mat), len(mat[0])
        soldiers_by_row = {}
        weakest_rows = [i for i in range(0, n)]

        for i in range(0, m):
            l, h = 0, n - 1
            soldiers_by_row[i] = 0
            marked_soldier_pos = 0

            while l <= h:
                mid = (l + h) // 2
                if mat[i][mid] > 0:
                    soldiers_by_row[i] += mid - marked_soldier_pos + 1
                    marked_soldier_pos = mid + 1
                    l = mid + 1
                elif mat[i][mid] == 0:
                    h = mid - 1

            # max_soldiers = soldiers_by_row[0]
            # for i in range(1, n):
            #     if soldiers_by_row[i] >= max_soldiers:
            #         max_soldiers = soldiers_by_row[i]

        return soldiers_by_row

 #    print(kWeakestRows([[1,0,0,0],
 # [1,1,1,1],
 # [1,0,0,0],
 # [1,0,0,0]], 2))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
