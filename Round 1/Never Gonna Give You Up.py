"""
Problem:
    Nobita is a student who is terrible at studying, he often fails his exam in school. Despite failing often, he does not give up at all and continues to retake his exam until he passes it.

    Given Nobita's chance of passing p, how many times does Nobita need to take the exam to have an at least 99% chance of passing?

Input Format:
    Nobita's chance of passsing his exam, p

Constraints:
    0 < p <= 1

Output Format:
    A single integer representing the number of times Nobita need to take the exam to have at least 99% chance of passing

Sample Input 0:
    0.9

Sample Output 0:
    2
"""

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def nobita_pass(p):
    return math.ceil(math.log(1 - 0.99) / math.log(1 - p))

if __name__ == '__main__':
    p = float(input().strip())
    exam_failures = nobita_pass(p)
    print(exam_failures)