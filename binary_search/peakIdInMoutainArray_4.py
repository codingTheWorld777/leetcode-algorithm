"""
An array arr a mountain if the following properties hold:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

**Example 1:**
Input: arr = [0,1,0]
Output: 1

**Example 2:**
Input: arr = [0,2,1,0]
Output: 1

**Example 3:**
Input: arr = [0,10,5,2]
Output: 1
"""


def peakIndexInMountainArray(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] > arr[middle - 1] and arr[middle] > arr[middle + 1]:
            return middle
        elif arr[middle - 1] > arr[middle]:
            high = middle
        elif arr[middle] < arr[middle + 1]:
            low = middle + 1