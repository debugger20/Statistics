
# The normal distribution refers to a family of continuous probability distributions described by the normal equation.
# The probability density of normal distribution is:

# N(x, μ, σ) = { 1 / [σ * sqrt(2 * pi)] } * e^-(x-μ)^2 / 2σ^2
# The graph of normal distribution depends on two factors:
# the mean and the standard deviation.
# the mean determines the center of the graph.
# the standard deviation determines the height and width.
# when the deviation is large, the curve is short and wide
# when the deviation is small, the curve is tall and narrow.
# All normal distributions look like symmetric, and bell-shaped.


# The total area under the normal curve is equal to 1.
# The probability that a normal random variable X equals any particular value is 0.
# The probability that X is greater than a equals the area under the normal curve bounded by a and plus infinity.
# The probability that X is less than a equals the area under the normal curve bounded by a and minus infinity.

# Every normal curve conforms the following rule:
# %68 of the area under the curve falls within 1 standard deviation of the mean.
# %95 of the area under the curve falls within 2 standard deviation of the mean.
# %99.7 of the area under the curve falls within 3 standard deviation of the mean.


# The cumulative distribution function for a function with normal distribution is:
# cum(x) = 1/2 (1 + erf(x-mean/stddev*sqrt(2)) )
# erf(z) = 2/pi 0-z[e^-x^2]dx

# Example:
# An average light bulb manufactured by the Acme Corporation lasts 300 days with a standard deviation of 50 days.
# Assuming that bulb life is normally distributed, what is the probability that an Acme light bulb will last at most 365 days?
# x = 365
# mean = 300
# stddev = 50
# P(X <= 365)


import math
from scipy.integrate import quad


def integrand(x):
    return math.e**(-(x**2))

def erf(z):
	res, err = quad(integrand, 0, z)
	return (2 / (math.pi**0.5)) * res

def cum(x, mean, stddev):
	return (1/2) * (1 + erf( (x-mean) / (stddev * (2**0.5) ) ) ) 

def normal(x, mean, stddev):
	return (1 / (stddev * ((2 * math.pi)**0.5))) * (math.e**(-1 * ((x-mean)**2) / (2 * (stddev**2))) )

print(cum(365, 300, 50)) # 0.90




# Second Example:
# In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
# What is the probability that a car can be assembled at this plant in:
# 1. Less than 19.5 hours?
# Between 20 and 22 hours?

avg = 20
stddev = 2
print("{0:.3f}".format(cum(19.5, avg, stddev)))
print("{0:.3f}".format(cum(22, avg, stddev) - cum(20, avg, stddev)))