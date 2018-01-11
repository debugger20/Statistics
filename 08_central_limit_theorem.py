
# The Central Limit Theorem states that, for a large enough sample(n), the distribution of sample mean will approach normal distribution.
# Let { X1, X2, X3, , Xn } be a random data set of size n.
# The sample average is (Total Xi / N)

# For large n, the distribution of sample sums Sn is close to normal distribution N(avg1, stddev1)
# avg1 = n * avg
# stddev1 = sqrt(n) * stddev


# Example: 
# A large elevator can transport a maximum of 9800 pounds.
# Suppose a load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds.
# Based on this information, what is the probability that all  boxes can be safely loaded into the freight elevator and transported?

# Distribution of sample sums will be close to normal distribution.
# X = 9800
# mean = 49 * 205
# stddev = sqrt(49) * 15

import math

def cum(x, mean, stddev):
	return (1/2) * (1 + math.erf( (x-mean) / (stddev * (2**0.5) ) ) ) 

def normal(x, mean, stddev):
	return (1 / (stddev * ((2 * math.pi)**0.5))) * (math.e**(-1 * ((x-mean)**2) / (2 * (stddev**2))) )

n = 49
X = 9800
avg = n * 205
stddev = math.sqrt(n) * 15

print("{0:.4f}".format(cum(X, avg, stddev)))