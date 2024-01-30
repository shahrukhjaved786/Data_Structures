"""
Given an array of positive numbers and a positive number ‘k’,
find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], K=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], K=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


def max_sum_K_size_sub_array(arr, K):
    max_sum = 0
    sub_arr = []
    wStart = 0
    wSum = 0
    for wEnd in range(0, len(arr)):
        wSum = wSum + arr[wEnd]

        if wEnd >= K - 1:
            if wSum >= max_sum:
                max_sum = wSum
                sub_arr = arr[wStart:wEnd+1]

            wSum = wSum - arr[wStart]
            wStart = wStart + 1

    return max_sum, sub_arr


print(max_sum_K_size_sub_array(arr=[2, 1, 5, 1, 3, 2], K=3))
print(max_sum_K_size_sub_array(arr=[2, 3, 4, 1, 5], K=2))
