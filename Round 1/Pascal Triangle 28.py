"""
Problem:
    Given an integer n, return the first n of Pascal's Triangle. 
    In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input Format:
    a single integer n

Constraints:
    1 <= n <= 30

Output Format:
    sequence of numbers seperated by spaces

Sample Input 0:
    3

Sample Output 0:
    1
    1 1
    1 2 1
"""

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def pascal(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)

    return "\n".join(" ".join(str(x) for x in r) for r in triangle)
    
if __name__ == '__main__':
    n = int(input().strip())
    output = pascal(n)
    print(output)