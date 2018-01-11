
# Covariance:
# Measure of how two random variables change together.
# The strength of their correlation.

# cov(X,Y) = 1/n * { for(i->n) (xi - avg_x) * (yi - avg_y) }

# Pearson Correlation Coefficient:
# p(X, Y) = cov(X,Y) / (std_X * std_Y)

n = int(input().strip())
X = [ float(el) for el in input().strip().split(' ') ]
Y = [ float(el) for el in input().strip().split(' ') ]

def stddev(nums):
	n = len(nums)
	mean = sum(nums) / n
	variance = sum( (x - mean)**2 for x in nums ) / n
	ss = variance**0.5
	return ss

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def cov(X, Y):
	avg_X = mean(X)
	avg_Y = mean(Y)
	total = 0

	for i in range(0, len(X)):
		total += (X[i] - avg_X) * (Y[i] - avg_Y)

	return (1/len(X)) * total

def pearson(X, Y):
	stdX = stddev(X)
	stdY = stddev(Y)
	return cov(X,Y) / (stdX * stdY)

print("{0:.3f}".format(pearson(X, Y)))