"""
Given an array, find the average of all contiguous sub-arrays of size ‘K’ in it.

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

"""


def K_size_sub_array_average(arr, K):
    average_list = []
    sub_arr = []
    for value_i in range(0, len(arr) - K + 1):
        current_sum = sum(arr[value_i:value_i + K])
        average_list.append(current_sum / K)
        sub_arr.append(arr[value_i:value_i + K])
    return average_list, sub_arr


average_result, sub_arrays = K_size_sub_array_average(arr=[1, 3, 2, 6, -1, 4, 1, 8, 2], K=5)
print(average_result)
print(sub_arrays)