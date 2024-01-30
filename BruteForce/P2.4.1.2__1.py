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


def longest_substring_K_chars(_str, K):
    max_len = 0
    longest_possible_substring = []
    for value_i in range(0, len(_str)):
        current_len = 0
        substring = set()
        for value_j in range(value_i, len(_str)):
            substring.add(_str[value_j])
            if len(substring) <= K:
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


print(longest_substring_K_chars(_str="araaci", K=2))
print(longest_substring_K_chars(_str="araaci", K=1))
print(longest_substring_K_chars(_str="cbbebi", K=3))
