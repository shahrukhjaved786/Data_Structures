"""
Given an array of characters where each character represents a fruit tree,
you are given two baskets and your goal is to put maximum number of fruits in each basket.
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree.
You will pick one fruit from each tree until you cannot, i.e.,
you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def maximum_number_fruits_in_baskets(fruits, baskets):
    max_fruit = 0
    longest_fruit_series = []
    fruit_map = {}
    wStart = 0
    for wEnd in range(0, len(fruits)):
        right_fruit = fruits[wEnd]

        if right_fruit not in fruit_map:
            fruit_map[right_fruit] = 0
        fruit_map[right_fruit] = fruit_map[right_fruit] + 1

        while len(fruit_map) > baskets:
            left_fruit = fruits[wStart]
            fruit_map[left_fruit] = fruit_map[left_fruit] - 1

            if fruit_map[left_fruit] == 0:
                del fruit_map[left_fruit]

            wStart = wStart + 1

        if wEnd - wStart + 1 > max_fruit:
            max_fruit = wEnd - wStart + 1
            longest_fruit_series = fruits[wStart: wEnd + 1]

    return max_fruit, longest_fruit_series


print(maximum_number_fruits_in_baskets(fruits=['A', 'B', 'C', 'A', 'C'], baskets=2))
print(maximum_number_fruits_in_baskets(fruits=['A', 'B', 'C', 'B', 'B', 'C'], baskets=2))
