
# The Poisson Experiment has the following properties:
# 1. The outcome of each trial is either success or failure.
# 2. The average number of successes that occurs in a specified region is known.
# 3. The probability that a success will occur is proportional to the size of the region.


# Poisson Distribution
# P(k, λ) = λ^k * e^-λ / k!

# e = 2.71828
# λ = average number of successes that occur in a specified region.
# k = the number of successes that occur in a specified region.
# P(k, λ) = Poisson probability, probability getting exactly k successes when average number of successes is λ.

# Example:
# ACME Realty company sells an average of 2 homes per day.
# What is the probability that exactly 3 homes will be sold tomorrow?
# P(k, λ) = λ^k * e^-λ / k!
# P(3, 2) = 2^3 * e^-2 / 3! = 0.180

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def poisson(k, lam):
	return (lam**k) * (math.e**(-lam)) / factorial(k)

lam = 2.5
k = 5

print("{0:.3f}".format(poisson(k, lam)))