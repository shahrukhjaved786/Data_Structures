"""
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""


def longest_substring_no_repeat_char(_str):
    max_len = 0
    longest_possible_substring = []
    freq_map = {}
    wStart = 0
    for wEnd in range(0, len(_str)):
        right_char = _str[wEnd]
        if right_char in freq_map:
            # this ensures that the start index of the current window
            # is adjusted to the right of the "last occurrence" of the current character
            wStart = max(wStart, freq_map[right_char] + 1)

        # this updates the frequency map with the "most recent position" of the current character in the string
        freq_map[right_char] = wEnd

        if wEnd - wStart + 1 >= max_len:
            if wEnd - wStart + 1 == max_len:
                longest_possible_substring.append(_str[wStart:wEnd + 1])
            else:
                longest_possible_substring = [_str[wStart:wEnd + 1]]

            max_len = wEnd - wStart + 1

    return max_len, longest_possible_substring


print(longest_substring_no_repeat_char(_str="aabccbb"))
print(longest_substring_no_repeat_char(_str="abbbb"))
print(longest_substring_no_repeat_char(_str="abccde"))
