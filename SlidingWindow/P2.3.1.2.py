"""
Given an array of positive numbers and a positive number ‘S’,
find the length of the smallest contiguous sub-array whose sum is greater than or equal to ‘S’.
Return 0, if no such sub-array exists.

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest sub-array with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest sub-arrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""
import math


def smallest_sum_S_sub_array(arr, S):
    min_len = math.inf
    sub_arr = []
    wStart = 0
    wSum = 0
    for wEnd in range(0, len(arr)):
        wSum = wSum + arr[wEnd]

        while wSum >= S:
            # min_len = min(min_len, wEnd - wStart + 1)
            if wEnd-wStart+1 <= min_len:

                if wEnd-wStart+1 == min_len:
                    sub_arr.append(arr[wStart:wEnd+1])
                else:
                    sub_arr = [arr[wStart:wEnd+1]]

                min_len = wEnd - wStart + 1

            wSum = wSum - arr[wStart]
            wStart = wStart + 1

    if min_len == math.inf:
        return 0
    else:
        return min_len,sub_arr


print(smallest_sum_S_sub_array(arr=[2, 1, 5, 2, 3, 2], S=7))
print(smallest_sum_S_sub_array(arr=[2, 1, 5, 2, 8], S=7))
print(smallest_sum_S_sub_array(arr=[3, 4, 1, 1, 6], S=8))
print(smallest_sum_S_sub_array(arr=[3, 4, 1, 1, 2], S=15))
