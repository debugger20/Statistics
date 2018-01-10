
# Negative Binomial Experiment

# It is a statistical experiment that has the following properties:
# 1. The experiment consists of x repeated trials.
# Each trial can result in just two possible outcomes. We call one of these outcomes a success and the other, a failure.
# The probability of success, denoted by P, is the same on every trial.
# The trials are independent; that is, the outcome on one trial does not affect the outcome on other trials.
# The experiment continues until r successes are observed, where r is specified in advance

# For Example:
# Flip a coin repeatedly and count the number of times the coin lands on heads.
# You continue flipping the coin until it has landed 5 times on heads.

# The negative binomial probability of getting the second head on the sixth flip of the coin is 0.078125.
# b*(x; r, P) = x-1Cr-1 * P^r * (1-P)^(x-r)
# b*(x; r, P) = { (x-1)! / (x-r-2)! * (r-1)! } * P^r * (1-P)^(x-r)

# Theoratically, negative binomial probability is the probability of having
# x-1 successes after n-1 and having x successes after n trials.


# Geometric Distribution
# It is a special case of the negative binomial distribution
# that deals the number of Bernoulli trials required to get a success.

# g(n,p) = q^(n-1) * p

# For example:
# Bob is a high school basketball player. He is a 70% free throw shooter.
# That means his probability of making a free throw is 0.70. During the season
# What is the probability that Bob makes his first free throw on his fifth shot?
# b*(5; 1, 0.7) = g(5, 0.7)

# TASK
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the 5th inspection?

# b*(5; 1, 1/3)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
	return factorial(n) / (factorial(n-r) * factorial(r))

def negative_binomial(x, r, p):
	return combination(x-1, r-1) * (p**r) * ((1-p)**(x-r))

pDefect = 1/3
x = 5
r = 1

print("{0:.3f}".format(negative_binomial(x, r, pDefect)))