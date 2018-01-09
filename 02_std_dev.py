
# The input should like that:
# N
# a0 a1 a2 ... a(N-1)
#
# The output:
# SDEV


import sys

n = int(input().strip())
nums = [int(arr_temp) for arr_temp in input().strip().split(' ')]

mean = sum(nums) / n

variance = sum( (x - mean)**2 for x in nums ) / n

ss = variance**0.5
print("{0:.1f}".format(ss))