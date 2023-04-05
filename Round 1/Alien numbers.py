# Problem:
# Scientist have discovered alien numbers that are represented by seven different symbols: Q, W, E, R, T, Y and U
# Q=1, W=5, E=10, R=50, T=100, Y=500, U=1000
# The scientist also found that the numerals are written in a weird way. the numeral for four is not QQQQ. Instead, the number four is written as QW. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as QE. There are six instances where subtraction is used:
# Q can be placed before W (5) and E (10) to make 4 and 9.
# E can be placed before R (50) and T (100) to make 40 and 90.
# T can be placed before Y (500) and U (1000) to make 400 and 900.

# Input Format:
# string s

# Constraints:
# s contains only the characters ('Q', 'W', 'E', 'R', 'T', 'Y', 'U').

# it is guaranteed that s is a valid numeral in the range [1, 3999].

# Output Format:
# a single integer representing s

# Sample Input 0:
# UTUETQW

# Sample Output 0:
# 1994

# Explanation 0:
# U = 1000, TU = 900, ET = 90 and QW = 4
# UTUETQW = 1994

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def alien(s: str) -> int:
    alien_map = {
        'Q': 1,
        'QW': 4,
        'W': 5,
        'QE': 9,
        'E': 10,
        'ER': 40,
        'R': 50,
        'ET': 90,
        'T': 100,
        'TY': 400,
        'Y': 500,
        'TU': 900,
        'U': 1000,
    }

    res = 0

    for i in range(len(s)):
        if i + 1 < len(s) and alien_map[s[i]] < alien_map[s[i + 1]]:
            res -= alien_map[s[i]]
        else:
            res += alien_map[s[i]]

    return res

if __name__ == '__main__':
    s = input()
    res = alien(s)
    print(res)