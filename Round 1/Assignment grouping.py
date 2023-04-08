"""
Problem:
    A lecturer wants to prepare team assignment topics. There are n groups of students that need to be teamed up. The *i*th group has si friends (1<=si<=4) who must go together. Each assignment team has at most 4 students. 
    
    What is the minimum number of topics that the lecturer must prepare?

Input Format
    n, the number of student groups
    a sequence of n integers representing the number of students in each group.

Constraints
    1<=si<=4 1<=n<=10000

Output Format
    integer representing the minimum number of assignment topics

Sample Input 0
    5
    1 2 4 3 3

Sample Output 0
    4

Explanation 0
    the first 2 group will team up and the rest of the groups are unchanged
"""
# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    # Write your code here