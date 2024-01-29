"""
Given an array, find the average of all contiguous sub arrays of size ‘K’ in it.

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""


def average_K_size_sub_array(arr, K):
    average_list = []
    sub_array = []
    wStart = 0
    wSum = 0

    for wEnd in range(0, len(arr)):
        wSum = wSum + arr[wEnd]

        if wEnd >= K - 1:
            average_list.append(wSum / K)
            sub_array.append(arr[wStart:wEnd + 1])

            wSum = wSum - arr[wStart]
            wStart = wStart + 1

    return average_list, sub_array


average_result,sub_arrays = average_K_size_sub_array(arr=[1, 3, 2, 6, -1, 4, 1, 8, 2], K=5)

print(average_result)
print(sub_arrays)