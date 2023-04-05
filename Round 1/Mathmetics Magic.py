# Problem:
# Given 3 numbers, what is the largest number you can get by adding either * or + between them. 
# You may also add brackets. The order of the numbers cannot be changed

# Input Format:
# 3 integers a,b,c seperated by space

# Constraints:
# 1 <= a, b, c <= 100

# Output Format:
# integer representing the largest possible result

# Sample Input 0:
# 2, 10, 3

# Sample Output 0:
# 60

# Explanation 0:
# 2 * 10 * 3 = 60

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def magic(a, b, c):
    return max(
        a + b + c,
        a * (b + c),
        (a + b) * c,
        a * b * c,
        (a * b) + c,
        a * (b * c),
        a + (b * c),
        (a + b) * c
    )

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    a = int(first_multiple_input[0])
    b = int(first_multiple_input[1])
    c = int(first_multiple_input[2])
    print(magic(a,b,c))