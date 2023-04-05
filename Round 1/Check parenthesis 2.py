# Problem:
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.. 
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input Format:
# string s

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'

# Output Format:
# print "true" if the parenthesis is valid, else "false"

# Sample Input 0:
# ()

# Sample Output 0:
# true

# Sample Input 1:
# (]

# Sample Output 1:
# false

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def checkParenthesis(string: str) -> bool:
    symbols = []
    for character in string:
        if character in ['(', '{', '[']:
            symbols.append(character)
        elif len(symbols) != 0:
            if character == ')' and symbols[-1] == '(':
                symbols.pop()
            elif character == '}' and symbols[-1] == '{':
                symbols.pop()
            elif character == ']' and symbols[-1] == '[':
                symbols.pop()
        else:
            return "false"
    if symbols == []:
        return "true"
    else:
        return "false"

if __name__ == '__main__':
    s = input()
    res = checkParenthesis(s)
    print(res)