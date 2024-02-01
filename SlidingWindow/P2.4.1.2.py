"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def longest_substring_K_distinct_chars(_str, K):
    max_len = 0
    substring = []
    freq_map = {}
    wStart = 0
    for wEnd in range(0, len(_str)):
        right_char = _str[wEnd]
        if right_char not in freq_map:
            freq_map[right_char] = 0
        freq_map[right_char] = freq_map[right_char] + 1

        # shrinking the window, until left with K characters in freq_map
        while len(freq_map) > K:
            left_char = _str[wStart]
            freq_map[left_char] = freq_map[left_char] - 1

            if freq_map[left_char] == 0:
                del freq_map[left_char]

            wStart = wStart + 1

        if wEnd - wStart + 1 >= max_len:
            if wEnd - wStart + 1 == max_len:
                substring.append(_str[wStart:wEnd + 1])
            else:
                substring = [_str[wStart:wEnd + 1]]

            max_len = wEnd - wStart + 1

    return max_len, substring


print(longest_substring_K_distinct_chars(_str="araaci", K=2))
print(longest_substring_K_distinct_chars(_str="araaci", K=1))
print(longest_substring_K_distinct_chars(_str="cbbebi", K=3))
