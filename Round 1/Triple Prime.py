"""
Problem:
    Alice and Bob are twin siblings who are both mathematics enthusiasts. Today, they come across a new concept called "triple prime".
    Alice explains to Bob that a triple prime is a number that is divisible by exactly three distinct positive integers. Bob gets excited and challenges Alice to a game. He will give her a number, and Alice has to tell him whether it is a triple prime or not.

    Can you help Alice by writing a program to determine if the number Bob gave her is a triple prime or not?

Input Format:
    integer i

Constraints:
    1 <= i <= 10000
    s consists of parentheses only '()[]{}'

Output Format:
    true if i is triple prime, false if it is not

Sample Input 0:
    4

Sample Output 0:
    true

Explanation 0:
    4 is divisible by 1, 2 and 4

Sample Input 1:
    5

Sample Output 1:
    false

Explanation 1
    5 is divisible 1 and 5
"""

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def triple_prime(i):
    divisors = 0
    for j in range(1, i + 1):
        if i % j == 0:
            divisors += 1
        if divisors > 3:
            return "false"
    return "true" if divisors == 3 else "false"

if __name__ == '__main__':
    i = int(input().strip())
    result = triple_prime(i)
    print(result)