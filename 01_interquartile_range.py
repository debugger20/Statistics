
# The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles.

# The input should like that:
# N (The number of elements)
# a0 a1 a2 ... a(N-1)  Numbers
# f0 f1 f2 ... f(N-1)  Frequencies

#
# The output:
# Interquartile range (answer should be rounded to a scale of 1 decimal place)

# Sample Input
# 6
# 6 12 8 10 20 16
# 5 4 3 2 1 5

# Output:
# 9.0


# 6 8 10 12 16 20
# 5 3  2  4  5  1


import sys

def calcQuartile(numsVSfreqs, size):
	currSize = int(size / 2)
	double = False
	nextKey = False
	val = 0

	if size % 2 == 0:
		double = True
	else:
		currSize += 1
	
	for key in sorted(numsVSfreqs.keys()):
		
		if nextKey:
			return (val + key) / 2
		elif numsVSfreqs[key] > currSize:
			return key
		elif numsVSfreqs[key] == currSize and not double:
			return key
		elif numsVSfreqs[key] == currSize and double:
			val = key
			nextKey = True
		else:
			currSize -= numsVSfreqs[key]


n = int(input().strip())
nums = [int(arr_temp) for arr_temp in input().strip().split(' ')]
freqs = [int(arr_temp) for arr_temp in input().strip().split(' ')]
totalSize = 0
numsVSfreqs = {}
upper = {}
lower = {}

for index, num in enumerate(nums):
	if num not in numsVSfreqs:
		numsVSfreqs[num] = freqs[index]
	else:
		numsVSfreqs[num] += freqs[index]		
	totalSize += freqs[index]

currSize = int(totalSize / 2)
atLower = True
rem = False
even = False
if totalSize % 2 == 0:
	even = True

for key in sorted(numsVSfreqs.keys()):
	if rem:
		rem = False
		upper[key] = numsVSfreqs[key] - 1
	elif numsVSfreqs[key] >= currSize and atLower and even:
		lower[key] = currSize
		upper[key] = numsVSfreqs[key] - currSize
		atLower = False
	elif numsVSfreqs[key] > currSize and atLower and not even:
		lower[key] = currSize
		upper[key] = numsVSfreqs[key] - currSize - 1
		atLower = False
	elif numsVSfreqs[key] == currSize and atLower and not even:
		lower[key] = currSize
		rem = True
		atLower = False
	elif atLower:
		lower[key] = numsVSfreqs[key]
		currSize -= numsVSfreqs[key]
	else:
		upper[key] = numsVSfreqs[key]


diff = calcQuartile(upper, int(totalSize / 2)) - calcQuartile(lower, int(totalSize / 2))
print("{0:.1f}".format(diff))