"""
Problem:
    Steve is a man that lives on his own out in the wild. One day, he stumbled upon a village and decided to live there. After talking to some villagers, he realized that emerald is the village's trading currency and being the most powerful person in the village is all about owning the most amount of emerald.

    He decided that he would only trade wheat because he thinks that would be the most profitable item to trade. With some close observation on wheat price, he would predict the price of wheat n day into the future.

    Given Steve's prediction on the wheat price p, Steve would like to know what is the maximum amount of profit he can make. At any point in time, Steve can only own a single wheat because he has no space to store them. However, he can buy and sell the wheat on the same day if needed. At this point in time, Steve has not started trading yet so he would need to buy the wheat first before being able to sell them.

Input Format:
    the number of days Steve predicted, n
    the price of wheat on each day, p

Constraints:
    1 <= n <= 1,000,000
    0 <= p <= 100

Output Format:
    a single integer representing the total profit

Sample Input 0:
    6
    1 2 3 1 2 3

Sample Output 0:
    4

Explanation 0:
    Day 1 - Steve buys wheat for the price of 1 
    Day 3 - Steve sells wheat for the price of 3, profit 2 
    Day 4 - Steve buys wheat again for the price of 1 
    Day 6 - Steve sells wheat for the price of 3, profit 2
    Total Profit: 2 + 2 = 4
"""

# Submission:
#!/bin/python3

import math
import os
import random
import re
import sys

def wheat(n, p):
    profit = 0
    buy_price = p[0]

    for i in range(1, n):
        if p[i] < buy_price:
            buy_price = p[i]
        else:
            profit += p[i] - buy_price
            buy_price = p[i]

    return profit

if __name__ == '__main__':
    n = int(input().strip())
    p = list(map(int, input().rstrip().split()))
    res = wheat(n, p)
    print(res)