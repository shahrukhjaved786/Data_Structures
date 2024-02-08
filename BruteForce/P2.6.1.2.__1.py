"""
Given a string, find the length of the longest substring which has no repeating characters.

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""


def longest_substring_no_repeat(_str):
    max_len = 0
    longest_possible_substring = []
    for value_i in range(0, len(_str)):

        current_len = 0
        substring = set()

        for value_j in range(value_i, len(_str)):

            if _str[value_j] not in substring:
                substring.add(_str[value_j])
                current_len = current_len + 1

                if current_len >= max_len:

                    if current_len == max_len:
                        longest_possible_substring.append(_str[value_i:value_j + 1])
                    else:
                        longest_possible_substring = [_str[value_i:value_j + 1]]

                    max_len = current_len
            else:
                break

    return max_len, longest_possible_substring


print(longest_substring_no_repeat(_str='aabccbb'))
print(longest_substring_no_repeat(_str='abbbb'))
print(longest_substring_no_repeat(_str='abccde'))
