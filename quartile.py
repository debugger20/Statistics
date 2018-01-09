
# The quartiles of an ordered data set are the  points that split the data set into  equal groups. The  quartiles are defined as follows:
# : The first quartile is the middle number between the smallest number in a data set and its median.
# : The second quartile is the median ( percentile) of the data set.
# : The third quartile is the middle number between a data set's median and its largest number.

# The input should like that:
# N
# a0 a1 a2 ... a(N-1)
#
# The output:
# Q1
# Q2
# Q3

# Sample Input
# 9
# 3 7 8 5 12 14 21 13 18

# Output:
# 6
# 12
# 16

import sys
import statistics

# Read the input and put it into nums list
n = int(input().strip())
nums = [int(arr_temp) for arr_temp in input().strip().split(' ')]

# sort and call median function of statistics
nums.sort()
print(int(statistics.median(nums[:int(n/2)])))
print(int(statistics.median(nums)))
print(int(statistics.median(nums[-int(n/2):])))