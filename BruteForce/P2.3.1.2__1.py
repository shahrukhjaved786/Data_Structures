"""
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous sub-array whose sum is greater than or equal to ‘S’.
Return 0, if no such sub-array exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest sub-arrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
import math


def smallest_sub_arr_S_sum(arr, S):
    min_len = math.inf
    sub_arr = []
    for value_i in range(0, len(arr)):
        current_sum = 0
        current_len = 0
        for value_j in range(value_i, len(arr)):
            if current_sum <= S:
                current_sum = current_sum + arr[value_j]
                current_len = current_len + 1

            if current_len <= min_len and current_sum >= S:
                if current_len == min_len:
                    sub_arr.append(arr[value_i:value_j + 1])
                else:
                    sub_arr = arr[value_i:value_j + 1]
                min_len = current_len

    if min_len == math.inf:
        return 0
    else:
        return min_len,sub_arr


print(smallest_sub_arr_S_sum(arr=[2, 1, 5, 2, 3, 2], S=7))
print(smallest_sub_arr_S_sum(arr=[2, 1, 5, 2, 8], S=7))
print(smallest_sub_arr_S_sum(arr=[3, 4, 1, 1, 6], S=8))
print(smallest_sub_arr_S_sum(arr=[2, 1, 3, 4, 2], S=15))
