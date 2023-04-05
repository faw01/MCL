# Problem:
# Anya, a child who can read mind, was adopted by a spy named Loid Forger. Loid's job is to carry out his mission wihtout revealing his own identity, therefore he frequently communicate with his secret ally in code.
# One day, Anya received Loid's letter from the mailman while he is not home. Being the little naughty child, she opens and tries to read the letter without his permission. Unsurprisingly, the letter was written in code, but she forgot that being able to read mind does not allow her to read code. She noticed there is a lot of parenthesis in the letter.
# Anya remembered something that she read from Loid's mind yesterday, it was something about receiving letter and then longest something?
# Anyway, this thing is too hard for Anya to understand. Given the content of the letter, can you help Anya decode the letter by finding the longest valid parenthesis?

# Input Format:
# the length of the letter, n
# the contents of the letter, c

# Constraints:
# 1 <= n <= 100,000
# c may only contain '[', ']'

# Output Format:
# A single integer of the longest valid parenthesis

# Sample Input 0:
# 5
# [[]][

# Sample Output 0:
# 4

# Explanation 0:
# [[]] is valid but [ is not, therefore the longest valid parenthesis is 4

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def loidCode(n, string):
    stack = []
    stack.append(-1)
    result = 0
 
    for i in range(n):
        if string[i] == '[':
            stack.append(i)
        else:
            if len(stack) != 0:
                stack.pop()

            if len(stack) != 0:
                result = max(result, i - stack[len(stack)-1])
            else:
               stack.append(i)
 
    return result

if __name__ == '__main__':
    n = int(input().strip())
    c = input()
    res = loidCode(n, c)
    print(res)