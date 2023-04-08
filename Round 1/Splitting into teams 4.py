"""
Problem:
    You are given a string s. Each character in s represents which class an element belongs to.
    You are required the partition s into as many substrings as possible.
    Each class can only be present in 1 substring
    The substrings must concatenate to the oringinal string s
    Return the maximum number of substrings

Input Format
    string s

Constraints
    1 <= s.length <= 500 s consists of lowercase English letters

Output Format
    a single integer representing the maximum number of substrings

Sample Input 0
    aabbcc

Sample Output 0
    3

Explanation 0
    The partition is "aa", "bb", "cc"

Sample Input 1
    abca

Sample Output 1
    1

Explanation 1
    you cannot split the string
"""

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def split(s):
    last_occurrence = {c: -1 for c in set(s)}

    for idx, char in enumerate(s):
        last_occurrence[char] = idx

    max_substrings_count = 0
    left_pointer, right_pointer = 0, 0

    for idx, char in enumerate(s):
        right_pointer = max(right_pointer, last_occurrence[char])

        if idx == right_pointer:
            max_substrings_count += 1
            left_pointer = idx + 1

    return max_substrings_count

if __name__ == '__main__':
    s = input().strip()
    result = split(s)
    print(result)