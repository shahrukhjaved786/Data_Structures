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


def max_sum_K_sub_array(arr, K):
    max_sum = 0
    sub_arr = []
    for value_i in range(0, len(arr) - K + 1):
        current_sum = 0
        for value_j in range(value_i, value_i + K):
            current_sum = current_sum + arr[value_j]
            if current_sum >= max_sum:
                max_sum = current_sum
                sub_arr = arr[value_i:value_j + 1]

    return max_sum, sub_arr


print(max_sum_K_sub_array(arr=[2, 1, 5, 1, 3, 2], K=3))
print(max_sum_K_sub_array(arr=[2, 3, 4, 1, 5], K=2))
